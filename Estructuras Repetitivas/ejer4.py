""""
Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se 
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.
"""
# Pedir al usuario que ingrese un número
numero = int(input("Ingresa el número para calcular su tabla de multiplicar: "))

# Recorrer los números del 1 al 10
for multiplicador in range(1, 11):
    # Calcular el producto del número y el multiplicador
    producto = numero * multiplicador
    # Imprimir el multiplicando, el multiplicador y el producto
    print(f"{numero} x {multiplicador} = {producto}")
