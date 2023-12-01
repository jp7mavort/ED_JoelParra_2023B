import math
#ejercicios por Joel Parra 


nombre = input("Ingrese el nombre de la persona: ")
apellido1 = input("Ingrese el primer apellido: ")
apellido2 = input("Ingrese el segundo apellido: ")


iniciales = nombre[0] + apellido1[0] + apellido2[0]


print(f"\nLas iniciales de la persona son: {iniciales.upper()}")
