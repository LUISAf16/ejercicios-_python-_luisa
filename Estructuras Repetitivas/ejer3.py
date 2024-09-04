""""
Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja 
de todo el grupo.
"""
# Inicializar variables para la suma de las calificaciones, 
# la calificación más alta y la calificación más baja.
suma = 0
calificacionMax = float('-inf')  # Inicializa con el valor más bajo posible
calificacionMin = float('inf')   # Inicializa con el valor más alto posible

# Utilizar un bucle 'for' para leer las calificaciones de 20 alumnos
for i in range(20):
    # Solicitar al usuario que ingrese la calificación de un alumno
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    
    # Añadir la calificación a la suma total para calcular el promedio más tarde
    suma += calificacion
    
    # Verificar si la calificación actual es la más alta hasta ahora
    if calificacion > calificacionMax:
        calificacionMax = calificacion
    
    # Verificar si la calificación actual es la más baja hasta ahora
    if calificacion < calificacionMin:
        calificacionMin = calificacion

# Calcular el promedio de las calificaciones
promedio = suma / 20

# Imprimir el promedio, la calificación más alta y la calificación más baja
print(f"El promedio de las calificaciones es: {promedio}")
print(f"La calificación más alta es: {calificacionMax}")
print(f"La calificación más baja es: {calificacionMin}")
