import math
#ejercicios por Joel Parra 


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))


mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)
medio = (numero1 + numero2 + numero3) - mayor - menor

print(f"\nNúmeros ordenados de mayor a menor: {mayor}, {medio}, {menor}")
