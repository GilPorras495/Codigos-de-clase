Vector_Numeros = []

print("Por favor ingrese el tamano de la lista en numeros enteros")
lista = int(input(f"Ingrese el valor "))

print("Por favor, ingrese los numeros enteros")

for i in range(lista):
    valor = int(input(f"ingrese el valor {i + 1}: "))
    Vector_Numeros.append(valor)

print("\n El vector ingresado es ", Vector_Numeros)