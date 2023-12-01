import math
#ejercicios por Joel Parra 

a = float(input("Ingrese la base del rectangulo: "))
b = float(input("Ingrese la altura del rectangulo: "))
c = float(input("Ingres el radio del circulo: "))
pi = 3.1415

d = (a+a)+(b+b)
e = a*b
f = pi * c * 2
g = pi * c * c

print("El perimetro de un rectangulo es:", d)
print("El area de un rectangulo es:", e)
print("El perimetro de un circulo es:", f)
print("El area de un circulo es:", g)