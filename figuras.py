from punto import *
from math import pi

class Figura:

    def __init__(self, p1, p2):
        self.origen = p1
        self.fin = p2
        self.area = 0
        self.perimetro = 0
        self.base = 0
        self.altura = 0


class Cuadrado(Figura):     #Herencia

    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.area = lado * lado

    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.perimetro = lado * 4


class Circulo(Figura):
    
    def calcular_area(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.area = pi * (radio ** 2)

    def calcular_perimetro(self):
        radio = self.origen.calcular_distancia(self.fin)
        self.perimetro = 2 * pi * radio


class Triangulo(Figura):
    
    def calcular_area(self):
        punto3 = Punto(self.origen.x, self.fin.y)
        self.base = punto3.calcular_distancia(self.fin)
        self.altura = punto3.calcular_distancia(self.origen)
        self.area = (self.base * self.altura)/2

    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.perimetro = lado + self.base + self.altura
        
