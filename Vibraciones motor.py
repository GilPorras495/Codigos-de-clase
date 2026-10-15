Lista_Vibraciones = []
print("Ingrese 5 valores de vibracion del motor industrial")

for Vibraciones in range(5):
    Vib = float(input(f"Medicion : {Vibraciones + 1} "))
    Lista_Vibraciones.append(Vib)

Lista_Prom = sum(Lista_Vibraciones) / len(Lista_Vibraciones)

if Lista_Prom > 4.0 :
    print(f"Vibraciones del motor peligrosas, valor {Lista_Prom:.2f}mm/s")
else:
    print(f"Las vibraciones estan en un rango normal, valor {Lista_Prom:.2} mm/s")