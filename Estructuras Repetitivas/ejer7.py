""""
La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad 
de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo 
dígito de la placa de cada carro, se puede determinar el color de la calcomanía 
utilizando la siguiente relación:

DIGITO   COLOR 
1 o 2    amarilla 
3 o 4    Rosa
5 o 6    Roja
7 o 8    Verde 
9 o 0    Azul
"""
# Solicitar al usuario el número total de autos
n = int(input("Ingresa el número total de autos que entran a la ciudad: "))

# comenzar el contador de cada color de calcomanía
calcomanias = {
    "amarilla": 0,
    "rosa": 0,
    "roja": 0,
    "verde": 0,
    "azul": 0}

# Iterar sobre el número total de autos para obtener el último dígito de cada placa
for i in range(n):
    ultimoDigito = int(input(f"Ingrese el último dígito de la placa del auto {i+1}: "))
    
    # Determinar el color de la calcomanía según el último dígito de la placa
    if ultimoDigito == 1 or ultimoDigito == 2:
        calcomanias["amarilla"] += 1
    elif ultimoDigito == 3 or ultimoDigito == 4:
        calcomanias["rosa"] += 1
    elif ultimoDigito == 5 or ultimoDigito == 6:
        calcomanias["roja"] += 1
    elif ultimoDigito == 7 or ultimoDigito == 8:
        calcomanias["verde"] += 1
    elif ultimoDigito == 9 or ultimoDigito == 0:
        calcomanias["azul"] += 1
    else:
        print("Último dígito inválido. Debe ser un número entre 0 y 9.")

# Mostrar el resultado
print("Resultados:")
print(f"Calcomanías amarillas: {calcomanias['amarilla']}")
print(f"Calcomanías rosas: {calcomanias['rosa']}")
print(f"Calcomanías rojas: {calcomanias['roja']}")
print(f"Calcomanías verdes: {calcomanias['verde']}")
print(f"Calcomanías azules: {calcomanias['azul']}")

