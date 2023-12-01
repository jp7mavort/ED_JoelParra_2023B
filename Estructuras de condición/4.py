import math
#ejercicios por Joel Parra 



A = float(input("Ingrese la longitud del lado A: "))
B = float(input("Ingrese la longitud del lado B: "))
C = float(input("Ingrese la longitud del lado C: "))

if A + B > C and A + C > B and B + C > A:
    if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
        tipo_trianguo = "triángulo rectángulo"
    elif A == B or A == C or B == C:
        tipo_trianguo = "triángulo isósceles"
    elif A == B == C:
        tipo_trianguo = "triángulo equilátero"
    else:
        tipo_trianguo = "triángulo escaleno"

    print(f"\nEl triángulo con lados de longitud {A}, {B}, {C} es un {tipo_trianguo}.")
else:
    print("\nLas dimensiones dadas no forman un triángulo válido.")
