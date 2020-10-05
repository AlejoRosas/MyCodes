class figuras():
    def __init__(self):
        self.area = 0

    def cuadrilatero(self, ladoA, ladoB):
        self.area = ladoA * ladoB
        return self.area

    def triangulo(self, base, altura):
        self.area = (base * altura)/2
        return self.area

    def circulo(self,radio):
        self.area = 3.1416 * (radio**2)
        return self.area

myFigura = figuras()
print(myFigura.cuadrilatero(4,4))
print(myFigura.triangulo(4,8))
print(myFigura.circulo(2))