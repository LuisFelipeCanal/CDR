# Definición de la clase Region
class Region:
    # Constructor de la clase Region
    def __init__(self, name):
        self.name = name  # Nombre de la región
        self.servers = []  # Lista de servidores en la región
        self.load_balancer = LoadBalancer()  # Instancia del balanceador de carga

    # Método para añadir un servidor a la región
    def add_server(self, server):
        self.servers.append(server)  # Añadir el servidor a la lista de servidores
        self.load_balancer.add_server(server)  # Añadir el servidor al balanceador de carga

    # Método para manejar una solicitud
    def handle_request(self, request):
        self.load_balancer.distribute_http_requests([request])  # Distribuir la solicitud usando el balanceador de carga


# Definición de la clase MultiRegionHA
class MultiRegionHA:
    # Constructor de la clase MultiRegionHA
    def __init__(self):
        self.regions = []  # Lista de regiones

    # Método para añadir una región
    def add_region(self, region):
        self.regions.append(region)  # Añadir la región a la lista de regiones

    # Método para enrutar una solicitud
    def route_request(self, request):
        # Simular el enrutamiento basado en disponibilidad y rendimiento
        primary_region = self.regions[0]  # Región primaria
        secondary_region = self.regions[1]  # Región secundaria
        try:
            primary_region.handle_request(request)  # Intentar manejar la solicitud en la región primaria
        except Exception as e:
            print(f"Primary region failed: {e}")  # Imprimir el error si la región primaria falla
            secondary_region.handle_request(request)  # Manejar la solicitud en la región secundaria

# Ejemplo de uso

# Crear instancias de regiones
region1 = Region("us-east-1")
region2 = Region("us-west-1")

# Crear instancias de servidores
server1 = Server("Server 1")
server2 = Server("Server 2")

# Añadir servidores a las regiones
region1.add_server(server1)
region2.add_server(server2)

# Crear una instancia del sistema MultiRegionHA
ha_system = MultiRegionHA()

# Añadir regiones al sistema
ha_system.add_region(region1)
ha_system.add_region(region2)

# Enrutar una solicitud usando el sistema
ha_system.route_request("Request 1")
