Names = []

print("Ingrese 5 nombres ")

for i in range(5):
    Name = input(f"Nombre {i + 1}: ")
    Names.append(Name)

Name_Buscar =  input("\n Ingresa el nombre que deseas buscar en el vector: ")

if Name_Buscar in Names:
    print(f"exito! el nombre {Name_Buscar} si se encontro en el vector")
else:
    print(f"Lo siento, el nombre a buscar {Name_Buscar} No se encuentra en el vector")
    