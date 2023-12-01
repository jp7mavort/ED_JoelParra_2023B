import math
#ejercicios por Joel Parra 

nota = float(input("Ingrese la nota: "))
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (F/M): ")


if nota >= 5 and edad >= 18:
    if sexo == 'F':
        mensaje = 'ACEPTADA'
    elif sexo == 'M':
        mensaje = 'POSIBLE'
    else:
        mensaje = 'NO ACEPTADA'
else:
    mensaje = 'NO ACEPTADA'

print(f"\n{mensaje}")
