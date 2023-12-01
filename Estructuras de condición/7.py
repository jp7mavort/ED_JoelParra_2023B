import math
#ejercicios por Joel Parra 

zona = int(input("Ingrese la zona a la que se enviará el paquete (1-5 1.AMerica del norte, 2. America central, 3.America del sur, 4. Europa, 5.Asia): "))
peso_paquete = float(input("Ingrese el peso del paquete en gramos: "))
costo_gramo = 0.0

if zona == 1:
    costo_gramo = 24.00
elif zona == 2:
    costo_gramo = 20.00
elif zona == 3:
    costo_gramo = 21.00
elif zona == 4:
    costo_gramo = 10.00
elif zona == 5:
    costo_gramo = 18.00

if peso_paquete > 5000:
    print("\nEl paquete no puede ser transportado debido a su peso superior a 5 kg.")
else:
    costo_total = peso_paquete * costo_gramo / 1000
    print(f"\nEl costo total de la entrega del paquete es: {costo_total:.2f} euros")
