class Dron:
    def __init__(self, id_dron):
        self.id = id_dron      
        self._bateria = 100   

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):

        if not valor or not str(valor).strip():
            raise ValueError("El identificador no puede estar vacío.")
        self.__id = str(valor).strip()

    def volar(self):
        print("El dron está volando")


class DronVigilancia(Dron):
    def volar(self):
        print("Dron de vigilancia sobrevolando perímetro")


class DronReparto(Dron):
    def volar(self):
        print("Dron de reparto entregando paquete")


dron_base = Dron("DRN-000")
dron_vigilante = DronVigilancia("DRN-VIG-01")
dron_repartidor = DronReparto("DRN-REP-02")

print("=== Vuelo de Drones ===")
dron_base.volar()
dron_vigilante.volar()
dron_repartidor.volar()