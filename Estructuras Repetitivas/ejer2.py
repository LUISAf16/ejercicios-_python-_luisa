""""
Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números
"""
# Empezamos la variable que almacenará la suma de los números convertidos a positivos
suma = 0

# Utilizar un bucle 'for' para repetir el proceso 10 veces
for i in range(10):
    # Solicitar al usuario que ingrese un número negativo
    numero = int(input(f"Ingrese el número negativo {i + 1}: "))
    
    # Verificar que el número ingresado sea negativo
    if numero < 0:
        # Convertir el número negativo a positivo
        numero = -numero
        # Agregar el número positivo a la suma acumulada
        suma += numero
    else:
        # Mensaje de advertencia si el número ingresado no es negativo
        print("Por favor, ingrese un número negativo.")
        # Restar uno al contador para asegurarse de que se lean 10 números negativos válidos
        i -= 1

# Imprimir el resultado final de la suma de los números positivos
print(f"La suma de los números convertidos a positivos es: {suma}")
