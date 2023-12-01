import math
#ejercicios por Joel Parra 

x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre los puntos ({",x1, "{",y1,"}) ({",x2,"}" "{",y2,"}) es:",distancia )
