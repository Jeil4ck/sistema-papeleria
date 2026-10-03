from app.database.conexion import Conexion
from app.services.inventario import InventarioService
from app.services.ventas import VentaService


def mostrar_menu():
    print("\n========================================")
    print("         SISTEMA DE PAPELERÍA")
    print("========================================")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar stock")
    print("5. Registrar venta")
    print("6. Eliminar producto")
    print("7. Salir")
    print("========================================")


def registrar_producto(inventario):

    print("\n========== REGISTRAR PRODUCTO ==========")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

        if stock < 0:
            print("El stock no puede ser negativo.")
            return

        exitoso, mensaje = inventario.agregar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        print(mensaje)

    except ValueError:
        print("El precio debe ser numérico y el stock debe ser un número entero.")


def mostrar_productos(inventario):

    print("\n========== INVENTARIO ==========")

    productos = inventario.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(f"\nCódigo: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[2]}")
        print(f"Precio: ${producto[3]:,.0f}")
        print(f"Stock: {producto[4]}")
        print("----------------------------------------")


def buscar_producto(inventario):

    print("\n========== BUSCAR PRODUCTO ==========")

    codigo = input("Ingrese el código: ")

    producto = inventario.buscar_producto(codigo)

    if producto:
        print("\nProducto encontrado:")
        print(f"Código: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[2]}")
        print(f"Precio: ${producto[3]:,.0f}")
        print(f"Stock: {producto[4]}")
    else:
        print("No se encontró ningún producto con ese código.")


def actualizar_stock(inventario):

    print("\n========== ACTUALIZAR STOCK ==========")

    codigo = input("Código del producto: ")

    producto = inventario.buscar_producto(codigo)

    if not producto:
        print("El producto no existe.")
        return

    print(f"\nProducto: {producto[1]}")
    print(f"Stock actual: {producto[4]}")

    print("\n1. Agregar unidades")
    print("2. Retirar unidades")

    opcion = input("Seleccione una opción: ")

    try:
        cantidad = int(input("Cantidad: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        if opcion == "1":
            cantidad = cantidad

        elif opcion == "2":
            cantidad = -cantidad

        else:
            print("Opción inválida.")
            return

        exitoso, mensaje = inventario.actualizar_stock(
            codigo,
            cantidad
        )

        print(mensaje)

    except ValueError:
        print("La cantidad debe ser un número entero.")


def registrar_venta(venta_service):

    print("\n========== REGISTRAR VENTA ==========")

    codigo = input("Código del producto: ")

    try:
        cantidad = int(input("Cantidad: "))

        exitoso, resultado = venta_service.registrar_venta(
            codigo,
            cantidad
        )

        if exitoso:
            print("\n========== VENTA REALIZADA ==========")
            print(f"Producto: {resultado['nombre']}")
            print(f"Cantidad: {resultado['cantidad']}")
            print(f"Precio unitario: ${resultado['precio']:,.0f}")
            print(f"TOTAL: ${resultado['total']:,.0f}")
            print(f"Stock restante: {resultado['stock_restante']}")

        else:
            print("\nNo se pudo realizar la venta.")
            print(resultado)

    except ValueError:
        print("La cantidad debe ser un número entero.")


def eliminar_producto(inventario):

    print("\n========== ELIMINAR PRODUCTO ==========")

    codigo = input("Ingrese el código del producto: ")

    producto = inventario.buscar_producto(codigo)

    if not producto:
        print("El producto no existe.")
        return

    print(f"\nProducto: {producto[1]}")

    confirmacion = input(
        "¿Está seguro de eliminarlo? (s/n): "
    )

    if confirmacion.lower() == "s":

        eliminado = inventario.eliminar_producto(codigo)

        if eliminado:
            print("Producto eliminado correctamente.")
        else:
            print("No fue posible eliminar el producto.")

    else:
        print("Operación cancelada.")


def main():

    base_datos = Conexion()
    base_datos.crear_tablas()

    inventario = InventarioService()
    venta_service = VentaService()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(inventario)

        elif opcion == "2":
            mostrar_productos(inventario)

        elif opcion == "3":
            buscar_producto(inventario)

        elif opcion == "4":
            actualizar_stock(inventario)

        elif opcion == "5":
            registrar_venta(venta_service)

        elif opcion == "6":
            eliminar_producto(inventario)

        elif opcion == "7":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()