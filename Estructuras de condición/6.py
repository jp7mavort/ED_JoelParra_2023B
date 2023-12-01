import math
#ejercicios por Joel Parra 

num_alumnos = int(input("Ingrese el número de alumnos que participarán en el viaje: "))
costo_por_alumno = 0
costo_renta_autobus = 0

if num_alumnos >= 100:
    costo_por_alumno = 65
elif 50 <= num_alumnos <= 99:
    costo_por_alumno = 70
elif 30 <= num_alumnos <= 49:
    costo_por_alumno = 95
else:
    costo_renta_autobus = 4000

total_pagar_autobus = costo_renta_autobus if costo_renta_autobus > 0 else num_alumnos * costo_por_alumno
costo_por_alumno = costo_por_alumno if costo_por_alumno > 0 else total_pagar_autobus / num_alumnos

print(f"\nTotal a pagar a la compañía de autobuses: {total_pagar_autobus} euros")
print(f"Costo individual por alumno: {costo_por_alumno:.2f} euros")
