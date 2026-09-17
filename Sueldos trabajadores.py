class Empleado:

  def __init__(self, nombre, salario_base):
    self.nombre = nombre
    self.salario_base = salario_base

  def calcular_salario(self):
    return self.salario_base


class Gerente(Empleado):

  def __init__(self, nombre, salario_base):
    super().__init__(nombre, salario_base)

  def calcular_salario(self):
    return self.salario_base + (self.salario_base * 0.30)


class Vendedor(Empleado):

  def __init__(self, nombre, salario_base, ventas):
    super().__init__(nombre, salario_base)
    self.ventas = ventas

  def calcular_salario(self):
    return self.salario_base + (self.ventas * 0.10)

trabajadores = [
  Empleado("Maldonado", 15000),
  Gerente("Gabriela", 30000),
  Vendedor("Gian", 12000, 5000)
]

for trabajador in trabajadores:
  print(
      f"{trabajador.nombre} ({type(trabajador).__name__}) gana:"
      f" ${trabajador.calcular_salario():.2f}"
  )