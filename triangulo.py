class Triangulo:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.area = 0

    def leer_datos(self):
        self.base = float(input("Ingresa la base del triángulo: "))
        self.altura = float(input("Ingresa la altura del triángulo: "))

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def imprimir_resultado(self):
        print(f"El área del triángulo con base {self.base} y altura {self.altura} es: {self.area}")

if __name__ == "__main__":
    t = Triangulo()
    t.leer_datos()
    t.calcular_area()
    t.imprimir_resultado()

