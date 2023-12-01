import math
#ejercicios por Joel Parra 


distancia = float(input("Ingrese la distancia entre los dos vehículos en kilómetros: "))
velocidad_1 = float(input("Ingrese la velocidad del vehículo 1 en km/h: "))
velocidad_2 = float(input("Ingrese la velocidad del vehículo 2 en km/h: "))

if velocidad_1 <= velocidad_2:
    print("\nEl vehículo 1 debe viajar a una velocidad mayor que el vehículo 2.")
else:
    
    tiempo_horas = distancia / (velocidad_1 - velocidad_2)

 
    tiempo_minutos = tiempo_horas * 60

  
    print(f"\nEl vehículo más rápido alcanzará al otro en {tiempo_minutos:.2f} minutos.")
