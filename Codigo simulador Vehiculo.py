import csv
import random

class base_de_datos:
    def __init__(self, reporte): 
        self.reporte = reporte

    def exportar_csv(self, interno, velocidades, limite):
        try:
            with open(self.reporte, mode='w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                
                escritor.writerow(["Limite de velocidad en la avenida en Km/h"])
                escritor.writerow(["Codigo Avenida", "Limite (km/h)"])
                for codigo, vel in limite.items():
                    escritor.writerow([codigo, vel])
                escritor.writerow([])

                escritor.writerow(["Congestionamiento en la avenida "])
                escritor.writerow(["Fila", "Columna", "Conteo Vehicular"])
                for inter in interno:
                    escritor.writerow([inter['fila'], inter['columna'], inter['vehiculos']])
                escritor.writerow([])

                escritor.writerow(["Velocidades en la avenida "])
                escritor.writerow(["Hora del Dia", "Velocidad Maxima Registrada"])
                for hora, velocidad in enumerate(velocidades):
                    escritor.writerow([f"{hora}:00", velocidad])

            print(f"\nReporte analítico exportado exitosamente a archivo CSV: {self.reporte}")
        except Exception as error: 
            print(f"Error al exportar el archivo CSV: {error}")

class SimuladorUrbano(base_de_datos):
    def __init__(self, filas, columnas, reporte="reporte_trafico.csv"):
        super().__init__(reporte)
        self.filas, self.columnas = filas, columnas
        
        self.matriz = [[random.randint(10, 800) for _ in range(columnas)] for _ in range(filas)]
        self.vector = [random.randint(40, 110) for _ in range(24)]  
        self.limites = {"AV_NORTE": 60, "AV_SUR": 80, "AV_ESTE": 50, "AV_OESTE": 70}

    def mostrar_matriz(self):
        print("Matriz del congestionamiento")
        [print(f"Fila {valor}:", row) for valor, row in enumerate(self.matriz)]
        print()

    def buscar_velocidad(self, objeto):
        print(f"Buscando velocidad {objeto} km/h en el vector...")
        encontrado = False
        for hora, velocidad in enumerate(self.vector):
            if velocidad == objeto:
                print(f"✅ Se encontro {objeto} km/h se registró a las {hora}:00 hrs.")
                encontrado = True
        
        if not encontrado:
            print(f"❌ No se encontro ninguna velocidad de {objeto} km/h no se registró en ningún horario.")
        print()

    def buscar_matriz(self, objeto):
        print(f"Buscando intersección con {objeto} vehículos en la matriz...")
        encontrado = False
        for posx, row in enumerate(self.matriz):
            for posy, value in enumerate(row):
                if value == objeto:
                    print(f"✅ Se encontro {objeto} vehículos en la posición Matriz[{posx}][{posy}].")
                    encontrado = True
        
        if not encontrado:
            print(f"❌ No se encontro ninguna intersección de la matriz registra exactamente {objeto} vehículos.")
        print()

    def _ordenar_burbuja(self, lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lista[j]["vehiculos"] < lista[j + 1]["vehiculos"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def analizar_flujo(self, vel_obj, matr_obj):
        self.mostrar_matriz()
        self.buscar_velocidad(vel_obj)
        self.buscar_matriz(matr_obj)
        
        planas = [{"fila": x, "columna": y, "vehiculos": self.matriz[x][y]} for x in range(self.filas) for y in range(self.columnas)]
        ordenadas = self._ordenar_burbuja(planas)
        
        print("Top Intersecciones con Mayor Congestión:")
        [print(f" > [{espacio['fila']}][{espacio['columna']}] - {espacio['vehiculos']} vehículos") for espacio in ordenadas[:5]]
        print()
        
        self.exportar_csv(ordenadas, self.vector, self.limites)

if __name__ == "__main__":
    print("Configuración del simulador")
    filas = int(input("Filas de la matriz (por defecto 3): ") or 3)
    columnas = int(input("Columnas de la matriz (por defecto 3): ") or 3)
    sim = SimuladorUrbano(filas, columnas)

    if input("¿Registrar matriz manualmente? (si/no): ").strip().lower() == 'si':
        for i in range(filas):
            for j in range(columnas):
                sim.matriz[i][j] = int(input(f"  -> Intersección [{i}][{j}]: "))

    velo_busq = int(input("Velocidad a buscar en el vector (por defecto 80): ") or 80)
    matr_busq = int(input("Vehículos a buscar en la matriz (por defecto toma el primero): ") or sim.matriz[0][0])
    
    print()
    sim.analizar_flujo(velo_busq, matr_busq)