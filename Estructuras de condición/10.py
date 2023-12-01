import math
#ejercicios por Joel Parra 


nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nota_ingles = float(input("Ingrese la nota de Inglés: "))


if 9 <= nota_ingles <= 10:
    mensaje = f"Felicitaciones, su nota es {nota_ingles}, equivalente a excelente"
elif 7 <= nota_ingles <= 8:
    mensaje = f"Siga adelante, su nota es {nota_ingles}, equivalente a muy buena"
elif 5 <= nota_ingles <= 6:
    mensaje = f"Debe esforzarse más, su nota es {nota_ingles}, equivalente a buena"
elif 0 <= nota_ingles <= 4:
    mensaje = f"Usted puede reprobar, su nota es {nota_ingles}, equivalente a regular"
else:
    mensaje = "Error: La nota ingresada no está en un rango válido (0-10)"


print(f"\n{nombre_estudiante}, {mensaje}")
