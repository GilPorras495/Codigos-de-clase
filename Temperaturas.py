List_Temps = [29.0, 10.5, 24.9, 30.8, 15.5, 5.5]
temperaturas_registradas = []

print("Acceso a los datos del sensor de temperatura")

for Temps in List_Temps:
    if Temps > 25:
        print("La temperatura es mayor al grado de seguridad es de ", Temps)
        temperaturas_registradas.append(Temps)