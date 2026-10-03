class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio:,.0f}")
        print(f"Stock: {self.stock}")

    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Se agregaron {cantidad} unidades.")
        else:
            print("La cantidad debe ser mayor que 0.")

    def reducir_stock(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0.")
        elif cantidad > self.stock:
            print("No hay suficiente stock.")
        else:
            self.stock -= cantidad
            print(f"Se retiraron {cantidad} unidades.")