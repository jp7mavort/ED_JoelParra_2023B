# Operadores in, not in, is, is not
lista = [1, 2, 3, 4, 5]
print(3 in lista)  # True
print("y" not in "Python")  # False

a = [1, 2, 3]
b = a
print(a is b)  # True
x = 5
y = 10
print(x is not y)  # True

# Comentarios
# Esto es un comentario de una sola línea
"""
Este es un comentario
de varias líneas
"""

# Tipos de Datos
numero_entero = 42
numero_largo = 1234567890123456789012345678901234567890
numero_flotante = 3.14
numero_complejo = 2 + 3j
verdadero = True
falso = False
cadena = "Hola, mundo!"
lista = [1, 2, 3, 4, 5]
tupla = (1, "dos", 3.0)
conjunto = {1, 2, 3, 4, 5}
diccionario = {"clave1": "valor1", "clave2": "valor2"}

# Convertir datos de str a int
numero_texto = "42"
numero_entero_convertido = int(numero_texto)
print(numero_entero_convertido)  # 42
