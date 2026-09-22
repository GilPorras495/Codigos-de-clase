class Actuador:
    def __init__(self, nombre):
        self.__nombre = nombre  
        self._estado = False   

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def activar(self):
        self._estado = True
        print("Actuador activado")

    def estado(self):
        if self._estado:
            print(f"El actuador '{self.__nombre}' está activo.")
        else:
            print(f"El actuador '{self.__nombre}' está inactivo.")

class Motor(Actuador):
    def girar(self):
        print("Motor girando a 100 RPM")


class Servo(Actuador):
    def mover_angulo(self, angulo):
        print(f"Servo movido a {angulo}°")

motor1 = Motor("Motor Principal")
servo1 = Servo("Micro Servo SG90")

print("Prueba del Motor")
motor1.estado()
motor1.activar()
motor1.estado()
motor1.girar()

print("\n Prueba del servo")
servo1.estado()
servo1.activar()
servo1.estado()
servo1.mover_angulo(90)