# 🏪 Sistema de Gestión para Papelería

Sistema de gestión desarrollado en Python para administrar el inventario y las ventas de una papelería.

El proyecto está siendo desarrollado como parte de mi aprendizaje en Ingeniería de Sistemas, aplicando conceptos de Programación Orientada a Objetos, bases de datos, arquitectura de software y control de versiones con Git.

---

## 📋 Descripción

El sistema permite administrar los productos de una papelería y registrar las ventas realizadas.

Actualmente funciona mediante una interfaz de consola y utiliza SQLite para almacenar la información de manera persistente.

---

## ✨ Funcionalidades actuales

### 📦 Gestión de productos

- Registrar productos.
- Mostrar el inventario.
- Buscar productos por código.
- Actualizar el stock.
- Eliminar productos.
- Validar códigos de producto duplicados.
- Evitar valores negativos en precio y stock.

### 🧾 Gestión de ventas

- Registrar una venta.
- Buscar el producto vendido.
- Verificar disponibilidad del stock.
- Calcular automáticamente el total.
- Descontar automáticamente las unidades vendidas.
- Guardar la venta en la base de datos.
- Mostrar el stock restante.

### 💾 Base de datos

El sistema utiliza SQLite para almacenar:

- Productos.
- Clientes.
- Ventas.

La base de datos local no se incluye en el repositorio mediante `.gitignore`.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.12**
- **SQLite**
- **Programación Orientada a Objetos (POO)**
- **Git**
- **GitHub**
- **Visual Studio Code**

---

## 📁 Estructura del proyecto

```text
sistema-papeleria/
│
├── app/
│   ├── database/
│   │   ├── __init__.py
│   │   └── conexion.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cliente.py
│   │   ├── producto.py
│   │   └── venta.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── inventario.py
│       └── ventas.py
│
├── docs/
├── tests/
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt