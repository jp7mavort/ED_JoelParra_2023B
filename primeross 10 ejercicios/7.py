import math
#ejercicios por Joel Parra 

numero = int(input("Ingrese un número de dos cifras: "))

if 10 <= numero <= 99:
    # Invertir las cifras directamente
    numero_invertido = int(str(numero)[::-1])

    print(f"\nEl número invertido de {numero} es: {numero_invertido}")
else:
    print("\nPor favor, ingrese un número de dos cifras.")