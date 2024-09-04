""""
 Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:
(1*2*3*4*5…).
"""
'''. Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:
(1*2*3*4*5…).'''
producto = 1

# Crear una variable para construir la cadena de multiplicación
multiplicacionCadena = ""

# Se egnera bucle para multiplicar los primeros 20 números naturales
for i in range(1, 21):  
    if i == 1:
        multiplicacionCadena += f"{i}"  # Comienza la cadena con el primer número
    else:
        multiplicacionCadena += f" * {i}"  # Añadir el siguiente número con un "*"

    producto *= i  # Actualizar el producto

# Imprimir la cadena de la multiplicación junto con el resultado final
print(f"{multiplicacionCadena} = {producto}")
