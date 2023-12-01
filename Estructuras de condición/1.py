import math
#ejercicios por Joel Parra 


cadena = input("Ingrese un caracter: ")


if len(cadena) == 1 and cadena.isalpha() and cadena.isupper():
    print(f"\nLa letra '{cadena}' es una letra mayúscula.")
else:
    print(f"\n'{cadena}' no es una letra mayúscula.")
