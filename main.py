if __name__ == "__main__":

    print("========== CLIENTE FÍSICO ==========")

    try:

        cliente1 = ClienteFisico(
            "Juan",
            "Perez",
            "40123456",
            "15/08/1995",
            "juan.perez@gmail.com",
            "+54 358 123-4567",
            "rio cuarto"
        )

        print(cliente1)
        print(repr(cliente1))

    except (TypeError, ValueError) as error:
        print("Error:", error)


    print("\n========== CLIENTE JURÍDICO ==========")

    try:

        cliente2 = ClienteJuridico(
            "Distribuidora Central",
            "ventas@distribuidora.com",
            "+54 358 555-5555",
            "rio cuarto",
            "30123456789",
            "Distribuidora Central SRL"
        )

        print(cliente2)
        print(repr(cliente2))

    except (TypeError, ValueError) as error:
        print("Error:", error)


    print("\n========== PROVEEDOR ==========")

    try:

        proveedor1 = Proveedor(
            "Bebidas del Centro SRL",
            "30987654321",
            "+54 358 444-4444",
            "ventas@bebidas.com",
            "cordoba"
        )

        print(proveedor1)
        print(repr(proveedor1))

    except (TypeError, ValueError) as error:
        print("Error:", error)


    print("\n========== CONTADORES ==========")

    print(
        "Cantidad de clientes:",
        Cliente.obtener_cantidad_clientes()
    )

    print(
        "Cantidad de proveedores:",
        Proveedor.obtener_cantidad_proveedores()
    )


    print("\n========== PRUEBA DNI INVÁLIDO ==========")

    try:

        cliente1.dni = "-40123456"

    except (TypeError, ValueError) as error:

        print("Validación correcta:", error)


    print("\n========== PRUEBA EMAIL INVÁLIDO ==========")

    try:

        cliente1.email = "juan@gmail"

    except (TypeError, ValueError) as error:

        print("Validación correcta:", error)


    print("\n========== PRUEBA TELÉFONO INVÁLIDO ==========")

    try:

        cliente1.telefono = "358+1234567"

    except (TypeError, ValueError) as error:

        print("Validación correcta:", error)


    print("\n========== PRUEBA FECHA INVÁLIDA ==========")

    try:

        cliente1.fecha_nacimiento = "40/15/2030"

    except (TypeError, ValueError) as error:

        print("Validación correcta:", error)