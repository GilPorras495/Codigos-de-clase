Vectores_Valor = []
suma_total = 0,0

print("Ingrese cuanto numeros decimales son")
lista = int(input(f"Ingrese los valores del vectores"))

for i in range(lista):
    numero = float(input(f"Elemento {i + 1}: "))
    Vectores_Valor.append(numero)

for elemento in Vectores_Valor:
    suma_total += elemento

print(f"\n Vector completo : {Vectores_Valor}")
print(f"La suma total de los elementos es : {suma_total}")