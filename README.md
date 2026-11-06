# Módulo Clientes - Programación 1

Este proyecto corresponde al módulo de clientes desarrollado como parte de la EFI de la materia Programación 1.

La EFI consiste en el desarrollo de un sistema básico para la gestión de un local de bebidas. Mi responsabilidad dentro del proyecto fue diseñar e implementar el módulo encargado de representar y validar la información de los clientes.

## Clase Cliente

La clase `Cliente` contiene los siguientes atributos:

- Nombre
- Apellido
- DNI
- Fecha de nacimiento
- Email
- Teléfono
- Localidad

Los atributos se encuentran encapsulados y son gestionados mediante `@property` y setters, donde se realizan distintas validaciones antes de almacenar los datos.

## Conceptos aplicados

Durante el desarrollo del módulo se aplicaron conceptos de Programación Orientada a Objetos en Python, entre ellos:

- Clases y objetos
- Encapsulamiento
- Properties
- Getters y setters
- Validación de datos
- Manejo de excepciones con `TypeError` y `ValueError`
- Atributos de clase
- Métodos de clase con `@classmethod`
- Métodos especiales `__str__` y `__repr__`
- Tipado
- Uso de `datetime` para validar fechas

## Contador de clientes

La clase posee el atributo de clase `_cantidad_clientes`, que permite registrar cuántas instancias de `Cliente` fueron creadas.

El valor puede consultarse mediante:

```python
Cliente.obtener_cantidad_clientes()
```

## Validaciones

El módulo incluye validaciones para evitar datos incorrectos, por ejemplo:

- DNI con formato incorrecto.
- Fechas inexistentes o futuras.
- Correos electrónicos sin dominio o extensión.
- Teléfonos con caracteres inválidos.
- Nombres, apellidos o localidades vacíos.

## Ejemplo

```python
cliente = Cliente(
    "Juan",
    "Perez",
    "40123456",
    "15/08/1995",
    "juan.perez@gmail.com",
    "+543581234567",
    "Rio Cuarto"
)

print(cliente)
```

## Contexto académico

Proyecto desarrollado como parte de la EFI de Programación 1, aplicando los fundamentos de Programación Orientada a Objetos en Python.
