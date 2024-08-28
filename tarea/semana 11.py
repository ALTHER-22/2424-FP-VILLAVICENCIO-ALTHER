# PROGRAMA 1: Búsqueda en Arreglo Multidimensional
# Crear una matriz bidimensional (3x3) con valores numéricos.
matriz = [
    [3, 7, 4],
    [8, 9, 6],
    [5, 1, 7]
]

# Búsqueda en la matriz para encontrar un valor específico que definas.
valor_buscado = 2

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if fila_encontrada != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.
if fila_encontrada != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")

# PROGRAMA 2: Ordenación de Arreglo Multidimensional

# Crear una matriz bidimensional (3x3) con valores numéricos.
matriz = [
    [9, 7, 2],
    [9, 4, 6],
    [2, 5, 3]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)
