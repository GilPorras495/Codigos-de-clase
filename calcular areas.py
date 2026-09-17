import math
class Figura:
    def area(self):
        return 0


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi*(self.radio**2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base*self.altura)/2

figuras = [
    Rectangulo(5, 10),      
    Circulo(3),            
    Triangulo(6, 4)        
]

for figura in figuras:
  
    print(f"El área de la figura {type(figura).__name__} es: {figura.area():.2f}")