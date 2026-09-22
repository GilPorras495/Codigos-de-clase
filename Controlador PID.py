class Controlador:
    def __init__(self, nombre, setpoint=0.0):
        self.__nombre = nombre         
        self._setpoint = float(setpoint)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def controlar(self):
        print("El controlador ajusta el sistema")

class ControladorPID(Controlador):
    def __init__(self, nombre, setpoint=0.0, kp=1.0, ki=0.1, kd=0.05):

        super().__init__(nombre, setpoint)
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def controlar(self):
        print("Aplicando control PID")


class ControladorOnOff(Controlador):
    def __init__(self, nombre, setpoint=0.0, histeresis=1.0):

        super().__init__(nombre, setpoint)
        self.histeresis = histeresis

    def controlar(self):
        print("Aplicando control On/Off")


control_base = Controlador("Controlador Genérico", setpoint=50.0)
pid = ControladorPID("PID Temperatura Horno", setpoint=180.0)
on_off = ControladorOnOff("Termostato Aire", setpoint=22.0)

print("=== Ejecución de Métodos controlar() ===")
print(f"Objeto: {control_base.nombre}")
control_base.controlar()

print(f"\nObjeto: {pid.nombre}")
pid.controlar()

print(f"\nObjeto: {on_off.nombre}")
on_off.controlar()