""""
Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos
neutros.
"""
# Inicializamos contadores para los números positivos, negativos y neutros
positivos = 0
negativos = 0
neutros = 0

# Usamos un bucle for para leer 20 números
for i in range(20):
    # Solicitamos al usuario que ingrese un número
    numero = float(input(f"Ingrese el número {i+1}: "))

    # Verificamos si el número es positivo
    if numero > 0:
        positivos += 1  # Incrementamos el contador de números positivos
    # Verificamos si el número es negativo
    elif numero < 0:
        negativos += 1  # Incrementamos el contador de números negativos
    # Si el número no es ni positivo ni negativo, es neutro (cero)
    else:
        neutros += 1  # Incrementamos el contador de números neutros

# Imprimimos los resultados
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
print(f"Cantidad de números neutros: {neutros}")
