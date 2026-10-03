from app.database.conexion import Conexion


class VentaService:

    def __init__(self):
        self.base_datos = Conexion()

    def registrar_venta(self, codigo_producto, cantidad):

        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()

        try:
            # Buscar el producto
            cursor.execute("""
                SELECT nombre, precio, stock
                FROM productos
                WHERE codigo = ?
            """, (codigo_producto,))

            producto = cursor.fetchone()

            if not producto:
                return False, "El producto no existe."

            nombre, precio, stock = producto

            # Validar cantidad
            if cantidad <= 0:
                return False, "La cantidad debe ser mayor que cero."

            # Verificar stock
            if cantidad > stock:
                return False, f"Stock insuficiente. Stock disponible: {stock}"

            # Calcular total
            total = precio * cantidad

            # Calcular nuevo stock
            nuevo_stock = stock - cantidad

            # Actualizar stock
            cursor.execute("""
                UPDATE productos
                SET stock = ?
                WHERE codigo = ?
            """, (nuevo_stock, codigo_producto))

            # Registrar venta
            cursor.execute("""
                INSERT INTO ventas
                (codigo_producto, cantidad, precio_unitario, total)
                VALUES (?, ?, ?, ?)
            """, (
                codigo_producto,
                cantidad,
                precio,
                total
            ))

            conexion.commit()

            return True, {
                "nombre": nombre,
                "cantidad": cantidad,
                "precio": precio,
                "total": total,
                "stock_restante": nuevo_stock
            }

        except Exception as error:

            conexion.rollback()

            return False, f"Error al registrar la venta: {error}"

        finally:
            conexion.close()