from figuras import *

p1 = Punto(5,5)
p2 = Punto(10,1)
cuadrado = Cuadrado(p1, p2)
circulo = Circulo(p1, p2)
triangulo = Triangulo(p1, p2)

cuadrado.calcular_area()
cuadrado.calcular_perimetro()
circulo.calcular_area()
circulo.calcular_perimetro()
triangulo.calcular_area()
triangulo.calcular_perimetro()

print "El area del cuadrado es: " + str(cuadrado.area)
print "El perimetro del cuadrado es: " + str(cuadrado.perimetro)
print "El area del circulo es: " + str(circulo.area)
print "La circunferencia es: " + str(circulo.perimetro)
print "El area del triangulo es: " + str(triangulo.area)
print "El perimetro del triangulo es: " + str(triangulo.perimetro)
