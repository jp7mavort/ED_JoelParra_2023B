import math
#ejercicios por Joel Parra 


numero_dia = int(input("Ingrese el número del día de la semana (1-7): "))

if numero_dia == 1:
    dia_semana = "Lunes"
elif numero_dia == 2:
    dia_semana = "Martes"
elif numero_dia == 3:
    dia_semana = "Miércoles"
elif numero_dia == 4:
    dia_semana = "Jueves"
elif numero_dia == 5:
    dia_semana = "Viernes"
elif numero_dia == 6:
    dia_semana = "Sábado"
elif numero_dia == 7:
    dia_semana = "Domingo"
else:
    print("Error: Por favor, ingrese un número válido del 1 al 7.")

if numero_dia in range(1, 8):
    print(f"\nEl día correspondiente al número {numero_dia} es: {dia_semana}")
