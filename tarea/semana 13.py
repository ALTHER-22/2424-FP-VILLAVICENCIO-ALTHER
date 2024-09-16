def calcular_temperaturas_promedio(ciudades_temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un período de tiempo.

    Args:
        ciudades_temperaturas (dict): Un diccionario donde las claves son nombres de ciudades (str)
                                      y los valores son listas de temperaturas (list de floats o ints).
                                      Cada lista representa las temperaturas registradas durante varias semanas.

    Returns:
        dict: Un diccionario donde las claves son los nombres de las ciudades y los valores son
              las temperaturas promedio calculadas para cada ciudad.
    """
    # Diccionario vacío para almacenar los promedios de temperatura por ciudad
    temperaturas_promedio = {}

    # Iteramos a través del diccionario de ciudades y sus temperaturas
    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Calculamos el promedio sumando todas las temperaturas y dividiendo por la cantidad de semanas
        promedio = sum(temperaturas) / len(temperaturas)

        # Guardamos el promedio en el nuevo diccionario usando la ciudad como clave
        temperaturas_promedio[ciudad] = promedio

    # Retornamos el diccionario que contiene las ciudades y sus promedios de temperatura
    return temperaturas_promedio


# Diccionario con ciudades y sus temperaturas semanales registradas
ciudades_temperaturas = {
    "Guayaquil": [29, 31, 29, 23, 28],  # Lista de temperaturas registradas en Guayaquil
    "Machala": [28, 30, 29, 31, 27],  # Lista de temperaturas registradas en Machala
    "Loja": [17, 18, 22, 23, 17],  # Lista de temperaturas registradas en Loja
    "Coca": [31, 29, 33, 28, 32],  # Lista de temperaturas registradas en Coca
    "Nueva Loja": [26, 28, 27, 29, 25]  # Lista de temperaturas registradas en Nueva Loja
}

# Llamamos a la función para calcular las temperaturas promedio de cada ciudad
promedios = calcular_temperaturas_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in promedios.items():
    # Formateamos la salida para mostrar las temperaturas promedio con dos decimales
    print(f"{ciudad}: {promedio:.2f}°C")