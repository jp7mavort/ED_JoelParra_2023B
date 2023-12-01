import math
#ejercicios por Joel Parra 


tipo_uva = input("Ingrese el tipo de uva (A o B): ").upper()
tamano_uva = int(input("Ingrese el tamaño de la uva (1 o 2): "))
kilos_uva = float(input("Ingrese la cantidad de kilos de uva entregados: "))

precio_inicial = 0.0

if tipo_uva == 'A':
    precio_inicial = 2.5
elif tipo_uva == 'B':
    precio_inicial = 1.8

if tipo_uva == 'A':
    if tamano_uva == 1:
        ganancia = kilos_uva * (precio_inicial + 0.2)
    elif tamano_uva == 2:
        ganancia = kilos_uva * (precio_inicial + 0.3)
else:
    if tamano_uva == 1:
        ganancia = kilos_uva * (precio_inicial - 0.3)
    elif tamano_uva == 2:
        ganancia = kilos_uva * (precio_inicial - 0.5)

print(f"\nLa ganancia obtenida por la entrega de {kilos_uva} kilos de uva tipo {tipo_uva} y tamaño {tamano_uva} es: ${ganancia:.2f}")
