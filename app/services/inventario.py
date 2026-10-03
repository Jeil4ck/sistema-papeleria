import sqlite3

from app.database.conexion import Conexion


class InventarioService:

    def __init__(self):
        self.base_datos = Conexion()

    def agregar_producto(self, codigo, nombre, categoria, precio, stock):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()

        try:
            # Verificar si el código ya existe
            cursor.execute("""
                SELECT codigo
                FROM productos
                WHERE codigo = ?
            """, (codigo,))

            producto_existente = cursor.fetchone()

            if producto_existente:
                return False, f"El código '{codigo}' ya está registrado."

            # Insertar el producto
            cursor.execute("""
                INSERT INTO productos
                (codigo, nombre, categoria, precio, stock)
                VALUES (?, ?, ?, ?, ?)
            """, (
                codigo,
                nombre,
                categoria,
                precio,
                stock
            ))

            conexion.commit()

            return True, f"Producto '{nombre}' agregado correctamente."

        except sqlite3.IntegrityError:
            conexion.rollback()
            return False, f"El código '{codigo}' ya está registrado."

        except Exception as error:
            conexion.rollback()
            return False, f"Error al agregar el producto: {error}"

        finally:
            conexion.close()

    def listar_productos(self):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT codigo, nombre, categoria, precio, stock
            FROM productos
            ORDER BY nombre
        """)

        productos = cursor.fetchall()

        conexion.close()

        return productos

    def buscar_producto(self, codigo):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT codigo, nombre, categoria, precio, stock
            FROM productos
            WHERE codigo = ?
        """, (codigo,))

        producto = cursor.fetchone()

        conexion.close()

        return producto

    def actualizar_stock(self, codigo, cantidad):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT stock
            FROM productos
            WHERE codigo = ?
        """, (codigo,))

        producto = cursor.fetchone()

        if not producto:
            conexion.close()
            return False, "El producto no existe."

        stock_actual = producto[0]
        nuevo_stock = stock_actual + cantidad

        if nuevo_stock < 0:
            conexion.close()
            return False, "El stock no puede ser negativo."

        cursor.execute("""
            UPDATE productos
            SET stock = ?
            WHERE codigo = ?
        """, (nuevo_stock, codigo))

        conexion.commit()
        conexion.close()

        return True, f"Stock actualizado. Nuevo stock: {nuevo_stock}"

    def eliminar_producto(self, codigo):
        conexion = self.base_datos.conectar()
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM productos
            WHERE codigo = ?
        """, (codigo,))

        conexion.commit()

        eliminado = cursor.rowcount > 0

        conexion.close()

        return eliminado