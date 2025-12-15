class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base*self.altura

    def perimetro(self):
        return 2*(self.base+self.altura)

class Triangulo(Figura):
    def __init__(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3

    def area(self):
        semiperimetro=(self.lado1+self.lado2+self.lado3)/2
        area=(semiperimetro*(semiperimetro - self.lado1)*(semiperimetro - self.lado2)*(semiperimetro - self.lado3))**0.5
        return area
    def perimetro(self):
        return self.lado1+self.lado2+self.lado3
        
class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return 3.1416*(self.radio**2)

    def perimetro(self):
        return 2*3.1416*self.radio

figuras = [
    Rectangulo(4, 5),
    Triangulo(3, 4, 5),
    Circulo(2)
]

for figura in figuras:
    print(type(figura).__name__)
    print("Area:", figura.area())
    print("Petímetro:", figura.perimetro())
    print("-" * 20)

