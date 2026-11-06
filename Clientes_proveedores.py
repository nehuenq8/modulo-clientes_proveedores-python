from datetime import datetime, date
#Estructura Cliente
class Cliente:
    _cantidad_clientes = 0
    def __init__(self, nombre: str, email: str, telefono: str, localidad: str) -> None:
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.localidad = localidad
        Cliente._cantidad_clientes += 1
         
#Getters y setters Nombre
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser un string")
        nuevo_nombre = nuevo_nombre.strip().title()
        if nuevo_nombre == "":
            raise ValueError("El campo nombre no puede estar vacío")
        if len(nuevo_nombre) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        if len(nuevo_nombre) > 50:
            raise ValueError("El nombre no puede tener más de 50 caracteres")
        self._nombre = nuevo_nombre
        
#Getters y setters de mail
    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, nuevo_email: str) -> None:
        if not isinstance(nuevo_email, str):
            raise TypeError("El mail debe ser un string")
        nuevo_email = nuevo_email.strip().lower()
        if " " in nuevo_email:
            raise ValueError("El mail no puede contener espacios")
        if nuevo_email.count("@") != 1:
            raise ValueError("El mail debe contener un solo '@'")
        usuario, dominio = nuevo_email.split("@")
        if len(usuario) < 2:
            raise ValueError("Debe haber al menos 2 caracteres antes del '@'")
        if "." not in dominio:
            raise ValueError("El dominio debe contener una extensión, por ejemplo '.com'")
        nombre_dominio, extension = dominio.rsplit(".", 1)
        if nombre_dominio == "":
            raise ValueError("Debe haber un dominio antes de la extensión")
        if len(extension) < 2:
            raise ValueError("La extensión del mail debe tener al menos 2 caracteres")
        self._email = nuevo_email
        
#Getters y setters del numero de telefono
    @property
    def telefono(self) -> str:
        return self._telefono
    @telefono.setter
    def telefono(self, nuevo_telefono: str) -> None:
        if not isinstance(nuevo_telefono, str):
            raise TypeError("El teléfono debe tener formato string")
        nuevo_telefono = (nuevo_telefono.strip().replace(" ", "").replace("-", ""))
        if nuevo_telefono == "":
            raise ValueError("El número de teléfono no puede estar vacío")
        if nuevo_telefono.startswith("+"):
            numero_sin_signo = nuevo_telefono[1:]
        else:
            numero_sin_signo = nuevo_telefono
        if not numero_sin_signo.isdigit():
            raise ValueError("El teléfono solo puede contener números " "y opcionalmente '+' al comienzo")
        if len(numero_sin_signo) < 8:
            raise ValueError("El número debe tener al menos 8 dígitos")
        if len(numero_sin_signo) > 15:
            raise ValueError("El número no puede tener más de 15 dígitos")
        self._telefono = nuevo_telefono
    
#Getters y setters de localidad
    @property
    def localidad(self) -> str:
        return self._localidad
    @localidad.setter
    def localidad(self, nueva_localidad: str) -> None:
        if not isinstance(nueva_localidad, str):
            raise TypeError("La localidad debe ser un string")
        nueva_localidad = nueva_localidad.strip().title()
        if nueva_localidad == "":
            raise ValueError("La localidad no puede estar vacía")
        self._localidad = nueva_localidad
        
    @classmethod
    def obtener_cantidad_clientes(cls) -> int:
        return cls._cantidad_clientes

        
class ClienteFisico(Cliente):
    def __init__(self, nombre: str, apellido: str, dni: str, fecha_nacimiento: str, email: str, telefono:str, localidad:str) -> None:
        super().__init__(nombre, email, telefono, localidad)   
        self.apellido = apellido
        self.dni = dni 
        self.fecha_nacimiento = fecha_nacimiento
        
#Getters y setters apellido
    @property
    def apellido(self) -> str:
        return self._apellido
    @apellido.setter
    def apellido(self, nuevo_apellido: str) -> None:
        if not isinstance(nuevo_apellido, str):
            raise TypeError("El apellido debe ser un string")
        nuevo_apellido = nuevo_apellido.strip().title()
        if nuevo_apellido == "":
            raise ValueError("El campo apellido no puede estar vacío")
        if len(nuevo_apellido) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres")
        if len(nuevo_apellido) > 50:
            raise ValueError("El apellido no puede tener más de 50 caracteres")
        self._apellido = nuevo_apellido
        
#Getters y setters DNI
    @property
    def dni(self) -> str:
        return self._dni

    @dni.setter
    def dni(self, nuevo_dni: str) -> None:
        if not isinstance(nuevo_dni, str):
            raise TypeError("El DNI debe ingresarse como string")
        nuevo_dni = nuevo_dni.strip()
        if not nuevo_dni.isdigit():
            raise ValueError("El DNI solo puede contener números")
        if int(nuevo_dni) <= 0:
            raise ValueError("El DNI debe ser mayor a 0")
        if len(nuevo_dni) != 8:
            raise ValueError("El DNI debe contener 8 dígitos")
        self._dni = nuevo_dni
        
#Getters y setters fecha de nacimiento
    @property
    def fecha_nacimiento(self) -> date:
        return self._fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha: str) -> None:
        if not isinstance(nueva_fecha, str):
            raise TypeError("La fecha de nacimiento debe ingresarse como string")
        try:
            fecha = datetime.strptime(nueva_fecha,"%d/%m/%Y").date()
        except ValueError:
            raise ValueError(
                "La fecha debe tener formato DD/MM/AAAA "
                "y debe ser una fecha válida"
            )
        if fecha > date.today():
            raise ValueError("La fecha de nacimiento no puede ser futura")
        self._fecha_nacimiento = fecha
        
    def __repr__(self) -> str:
        return (
            f"Cliente("
            f"'{self.nombre}', "
            f"'{self.apellido}', "
            f"{self.dni})"
        )


    def __str__(self) -> str:
        return (
            f"Cliente: {self.nombre} {self.apellido} | "
            f"DNI: {self.dni} | "
            f"Email: {self.email} | "
            f"Teléfono: {self.telefono} | "
            f"Localidad: {self.localidad}"
        )         
        
class ClienteJuridico(Cliente):
    def __init__(self, nombre: str, email:str, telefono:str, localidad:str, cuit: str, razon_social: str) -> None:
        super().__init__(nombre, email, telefono, localidad)
        self.cuit = cuit
        self.razon_social = razon_social
        
    @property
    def cuit(self) -> str:
        return self._cuit
    @cuit.setter
    def cuit(self, nuevo_cuit: str) -> None:
        if not isinstance(nuevo_cuit, str):
            raise TypeError("El CUIT debe ingresarse como string")
        nuevo_cuit = (nuevo_cuit.strip().replace("-", "").replace(" ", ""))
        if not nuevo_cuit.isdigit():
            raise ValueError("El CUIT solo puede contener números")
        if len(nuevo_cuit) != 11:
            raise ValueError( "El CUIT debe contener 11 dígitos")
        self._cuit = nuevo_cuit
        
    @property
    def razon_social(self) -> str:
        return self._razon_social
    @razon_social.setter
    def razon_social(self, nueva_razon_social: str) -> None:
        if not isinstance(nueva_razon_social, str):
            raise TypeError("La razón social debe ser un string")
        nueva_razon_social = nueva_razon_social.strip()
        if nueva_razon_social == "":
            raise ValueError("La razón social no puede estar vacía")
        self._razon_social = nueva_razon_social
        
    def __repr__(self) -> str:
            return (
                f"Cliente("
                f"'{self.nombre}', "
                f"'{self.cuit}', "
                f"{self.razon_social})"
            )
    
    
    def __str__(self) -> str:
        return (
                f"Cliente juridico: {self.nombre} | "
                f"Cuit: {self.cuit} | "
                f"Email: {self.email} | "
                f"Teléfono: {self.telefono} | "
                f"Localidad: {self.razon_social}"
        )

class Proveedor: 
    _cantidad_proveedores = 0
    def __init__(self, nombre_razon_social: str, cuit: str, telefono: str, email: str, localidad: str) -> None:
        self.nombre_razon_social = nombre_razon_social
        self.cuit = cuit
        self.telefono = telefono
        self.email = email
        self.localidad = localidad
        Proveedor._cantidad_proveedores += 1
    @property
    def nombre_razon_social(self) -> str:
        return self._nombre_razon_social
    @nombre_razon_social.setter
    def nombre_razon_social(self, nueva_razon_social: str) -> None:
        if not isinstance(nueva_razon_social, str):
            raise TypeError("La razón social debe ser un string")
        nueva_razon_social = nueva_razon_social.strip()
        if nueva_razon_social == "":
            raise ValueError("La razón social no puede estar vacía")
        self._nombre_razon_social = nueva_razon_social

    @property
    def cuit(self) -> str:
        return self._cuit
    @cuit.setter
    def cuit(self, nuevo_cuit: str) -> None:
        if not isinstance(nuevo_cuit, str):
            raise TypeError("El CUIT debe ingresarse como string")
        nuevo_cuit = (nuevo_cuit.strip().replace("-", "").replace(" ", ""))
        if not nuevo_cuit.isdigit():
            raise ValueError("El CUIT solo puede contener números")
        if len(nuevo_cuit) != 11:
            raise ValueError( "El CUIT debe contener 11 dígitos")
        self._cuit = nuevo_cuit       
        
    @property
    def telefono(self) -> str:
        return self._telefono
    @telefono.setter
    def telefono(self, nuevo_telefono: str) -> None:
        if not isinstance(nuevo_telefono, str):
            raise TypeError("El teléfono debe tener formato string")
        nuevo_telefono = (nuevo_telefono.strip().replace(" ", "").replace("-", ""))
        if nuevo_telefono == "":
            raise ValueError("El número de teléfono no puede estar vacío")
        if nuevo_telefono.startswith("+"):
            numero_sin_signo = nuevo_telefono[1:]
        else:
            numero_sin_signo = nuevo_telefono
        if not numero_sin_signo.isdigit():
            raise ValueError("El teléfono solo puede contener números " "y opcionalmente '+' al comienzo")
        if len(numero_sin_signo) < 8:
            raise ValueError("El número debe tener al menos 8 dígitos")
        if len(numero_sin_signo) > 15:
            raise ValueError("El número no puede tener más de 15 dígitos")
        self._telefono = nuevo_telefono
        
    @property
    def email(self) -> str:
        return self._mail
    @email.setter
    def email(self, nuevo_email: str) -> None:
        if not isinstance(nuevo_email, str):
            raise TypeError("El mail debe ser un string")
        nuevo_email = nuevo_email.strip().lower()
        if " " in nuevo_email:
            raise ValueError("El mail no puede contener espacios")
        if nuevo_email.count("@") != 1:
            raise ValueError("El mail debe contener un solo '@'")
        usuario, dominio = nuevo_email.split("@")
        if len(usuario) < 2:
            raise ValueError("Debe haber al menos 2 caracteres antes del '@'")
        if "." not in dominio:
            raise ValueError("El dominio debe contener una extensión, por ejemplo '.com'")
        nombre_dominio, extension = dominio.rsplit(".", 1)
        if nombre_dominio == "":
            raise ValueError("Debe haber un dominio antes de la extensión")
        if len(extension) < 2:
            raise ValueError("La extensión del mail debe tener al menos 2 caracteres")
        self._email = nuevo_email

    @property
    def localidad(self) -> str:
        return self._localidad
    @localidad.setter
    def localidad(self, nueva_localidad: str) -> None:
        if not isinstance(nueva_localidad, str):
            raise TypeError("La localidad debe ser un string")
        nueva_localidad = nueva_localidad.strip().title()
        if nueva_localidad == "":
            raise ValueError("La localidad no puede estar vacía")
        self._localidad = nueva_localidad
        
    @classmethod
    def obtener_cantidad_proveedores(cls) -> int:
        return cls._cantidad_proveedores

    def __repr__(self) -> str:
        return (
            f"Proveedor("
            f"'{self.nombre_razon_social}', "
            f"'{self.cuit}')"
        )

    def __str__(self) -> str:
        return (
            f"Proveedor: {self.nombre_razon_social} | "
            f"CUIT: {self.cuit} | "
            f"Teléfono: {self.telefono} | "
            f"Localidad: {self.localidad}"
        )    
        
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
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
