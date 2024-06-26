# Definición de la clase Servidor
class Servidor:
    # Constructor de la clase Servidor
    def __init__(self, nombre):
        # Asignar el nombre del servidor
        self.nombre = nombre

    # Método para manejar una solicitud
    def manejar_solicitud(self, solicitud):
        # Imprimir un mensaje indicando que el servidor está manejando la solicitud
        print(f"{self.nombre} está manejando solicitud: {solicitud}")

# Definición de la clase BalanceadorDeCarga
class BalanceadorDeCarga:
    # Constructor de la clase BalanceadorDeCarga
    def __init__(self):
        # Inicializar la lista de servidores
        self.servidores = []

    # Método para agregar un servidor al balanceador de carga
    def agregar_servidor(self, servidor):
        # Agregar el servidor a la lista de servidores
        self.servidores.append(servidor)

    # Método para distribuir solicitudes HTTP entre los servidores
    def distribuir_solicitudes_http(self, solicitudes):
        # Iterar sobre las solicitudes
        for solicitud in solicitudes:
            # Seleccionar el primer servidor de la lista (simulación de selección de servidor)
            servidor = self.servidores[0]
            # Hacer que el servidor maneje la solicitud
            servidor.manejar_solicitud(solicitud)

# Definición de la clase Región
class Region:
    # Constructor de la clase Región
    def __init__(self, nombre):
        # Asignar el nombre de la región
        self.nombre = nombre
        # Inicializar la lista de servidores en la región
        self.servidores = []
        # Crear una instancia del balanceador de carga para la región
        self.balanceador_de_carga = BalanceadorDeCarga()

    # Método para agregar un servidor a la región
    def agregar_servidor(self, servidor):
        # Agregar el servidor a la lista de servidores en la región
        self.servidores.append(servidor)
        # Agregar el servidor al balanceador de carga de la región
        self.balanceador_de_carga.agregar_servidor(servidor)

    # Método para manejar una solicitud en la región
    def manejar_solicitud(self, solicitud):
        # Hacer que el balanceador de carga de la región distribuya la solicitud
        self.balanceador_de_carga.distribuir_solicitudes_http([solicitud])

# Definición de la clase MultiRegionHA
class MultiRegionHA:
    # Constructor de la clase MultiRegionHA
    def __init__(self):
        # Inicializar la lista de regiones
        self.regiones = []

    # Método para agregar una región al sistema
    def agregar_region(self, region):
        # Agregar la región a la lista de regiones
        self.regiones.append(region)

    # Método para enrutar una solicitud entre las regiones
    def enrutar_solicitud(self, solicitud):
        # Seleccionar la región primaria y secundaria
        region_primaria = self.regiones[0]
        region_secundaria = self.regiones[1]
        try:
            # Intentar manejar la solicitud en la región primaria
            region_primaria.manejar_solicitud(solicitud)
        except Exception as e:
            # Imprimir un mensaje de error si la región primaria falla
            print(f"Región primaria falló: {e}")
            # Manejar la solicitud en la región secundaria
            region_secundaria.manejar_solicitud(solicitud)

# Ejemplo de uso

# Crear instancias de regiones
region1 = Region("us-east-1")
region2 = Region("us-west-1")

# Crear instancias de servidores
servidor1 = Servidor("Servidor 1")
servidor2 = Servidor("Servidor 2")

# Agregar servidores a las regiones
region1.agregar_servidor(servidor1)
region2.agregar_servidor(servidor2)

# Crear una instancia del sistema MultiRegionHA
ha_sistema = MultiRegionHA()

# Agregar regiones al sistema
ha_sistema.agregar_region(region1)
ha_sistema.agregar_region(region2)

# Enrutar una solicitud usando el sistema
ha_sistema.enrutar_solicitud("Solicitud 1")
