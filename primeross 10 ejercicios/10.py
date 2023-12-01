import math
#ejercicios por Joel Parra 


monedas_2euros = int(input("Ingrese la cantidad de monedas de 2 euros: "))
monedas_1euro = int(input("Ingrese la cantidad de monedas de 1 euro: "))
monedas_50cent = int(input("Ingrese la cantidad de monedas de 50 céntimos: "))
monedas_20cent = int(input("Ingrese la cantidad de monedas de 20 céntimos: "))
monedas_10cent = int(input("Ingrese la cantidad de monedas de 10 céntimos: "))


total_euros = (monedas_2euros * 2) + (monedas_1euro * 1) + (monedas_50cent * 0.5) + (monedas_20cent * 0.2) + (monedas_10cent * 0.1)
total_céntimos = total_euros * 100  3


print(f"\nTienes un total de {total_euros:.2f} euros y {int(total_céntimos)} céntimos.")
