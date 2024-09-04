""""
un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un 
algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e 
imprima:
• La cantidad de estudiantes que obtuvieron una calificación menor a 50. 
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero 
menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero 
menor que 80. 
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100
"""
# Comenzar contadores para cada rango de calificaciones
menosDe50 = 0
entre50Y69 = 0
entre70Y79 = 0
masDe80 = 0

# Bucle para leer las calificaciones de los 23 estudiantes
for i in range(23):
    # Solicitar al usuario la calificación del estudiante
    calificacion = int(input(f"Ingrese la calificación del estudiante {i+1} (entre 1 y 100): "))
    
    # Validar que la calificación esté en el rango correcto
    if calificacion < 1 or calificacion > 100:
        print("Calificación inválida. Debe estar entre 1 y 100.")
        continue
    
    # Clasificar la calificación en uno de los rangos
    if calificacion < 50:
        menosDe50 += 1
    elif 50 <= calificacion < 70:
        entre50Y69 += 1
    elif 70 <= calificacion < 80:
        entre70Y79 += 1
    else:
        masDe80 += 1

# Imprimir los resultados
print("\nResultados:")
print(f"Cantidad de estudiantes con calificación menor a 50: {menosDe50}")
print(f"Cantidad de estudiantes con calificación entre 50 y 69: {entre50Y69}")
print(f"Cantidad de estudiantes con calificación entre 70 y 79: {entre70Y79}")
print(f"Cantidad de estudiantes con calificación de 80 o más: {masDe80}")
