import math
import random

def distancia(ciudad1, ciudad2):
    # Calcula la distancia euclidiana entre dos ciudades
    return math.sqrt((ciudad2[0] - ciudad1[0])**2 + (ciudad2[1] - ciudad1[1])**2)

def costo_total(camino, distancias):
    # Calcula el costo total de un recorrido dado
    costo = 0
    for i in range(len(camino) - 1):
        costo += distancias[camino[i]][camino[i+1]]
    costo += distancias[camino[-1]][camino[0]]  # Suma la distancia de regreso a la ciudad de origen
    return costo

def recocido_simulado(distancias, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura):
    n = len(distancias)
    # Genera un recorrido inicial aleatorio
    camino_actual = list(range(n))
    random.shuffle(camino_actual)
    costo_actual = costo_total(camino_actual, distancias)
    mejor_camino = camino_actual[:]
    mejor_costo = costo_actual

    temperatura = temperatura_inicial
    for _ in range(iteraciones_por_temperatura):
        nueva_ciudad1 = random.randint(0, n-1)
        nueva_ciudad2 = random.randint(0, n-1)
        while nueva_ciudad2 == nueva_ciudad1:
            nueva_ciudad2 = random.randint(0, n-1)

        nuevo_camino = camino_actual[:]
        nuevo_camino[nueva_ciudad1], nuevo_camino[nueva_ciudad2] = nuevo_camino[nueva_ciudad2], nuevo_camino[nueva_ciudad1]
        nuevo_costo = costo_total(nuevo_camino, distancias)

        if nuevo_costo < costo_actual or random.random() < math.exp((costo_actual - nuevo_costo) / temperatura):
            camino_actual = nuevo_camino
            costo_actual = nuevo_costo

        if nuevo_costo < mejor_costo:
            mejor_camino = nuevo_camino
            mejor_costo = nuevo_costo

        temperatura *= factor_enfriamiento

    return mejor_camino, mejor_costo

# Ejemplo de uso
if __name__ == "__main__":
    # Definir las ciudades y sus posiciones (coordenadas x, y)
    ciudades = [(0, 0), (1, 2), (3, 1), (5, 3)]

    # Calcular las distancias entre las ciudades
    distancias = [[distancia(ciudades[i], ciudades[j]) for j in range(len(ciudades))] for i in range(len(ciudades))]

    # Parámetros del algoritmo de recocido simulado
    temperatura_inicial = 1000
    factor_enfriamiento = 0.95
    iteraciones_por_temperatura = 1000

    # Ejecutar el algoritmo de recocido simulado
    mejor_camino, mejor_costo = recocido_simulado(distancias, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura)

    print("Mejor recorrido encontrado:", mejor_camino)
    print("Costo del mejor recorrido:", mejor_costo)
