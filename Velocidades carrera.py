V_Carrera = []
print("Ingrese las velocidades de los corredores")

for Number in range(6):
    V = float(input(f"lectura {Number + 1}: "))
    V_Carrera.append(V)

V_max = max(V_Carrera)
V_min = min(V_Carrera)
V_Prom = sum(V_Carrera)/ len(V_Carrera)

print("De la carrera la mayor velocidad fue ",V_max," la menor ",V_min," y el promedio de la carrera fue de ",V_Prom)