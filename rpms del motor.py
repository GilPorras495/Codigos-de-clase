lista_rpm = []
print("Indique las revoluciones por minuto del motor")

for rpm in range(6):
    revoluciones = float(input(f"Marque la lectura {rpm + 1} de RPM: "))
    lista_rpm.append(revoluciones)


revoluciones_objetivo = float(input(f"Indique que velocidad busca "))
encontrar = False

for search in range(len(lista_rpm)):
    if lista_rpm[search] == revoluciones_objetivo:
        encontrar = True
        posicion = search
        break

print (f" De las lecturas marcadas el dia de hoy, {lista_rpm}")

if encontrar:
    print(f"Usted registro hoy la velocidad {revoluciones_objetivo}, en la posicion {posicion}")
else:
    print(f"No has registrado la velocidad {revoluciones_objetivo} el dia de hoy")