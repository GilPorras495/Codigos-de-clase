class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")


class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} tiene {self.edad} años y hace ¡Guau guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} tiene {self.edad} años y hace ¡Miau miau!")


class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} tiene {self.edad} años y hace ¡Muuuu!")

#Valores de prueba 

animales = [
  Perro("Firulais", 4),
  Gato("Michi", 2),
  Vaca("Lola", 5)
]

for animal in animales:
    animal.hacer_sonido()