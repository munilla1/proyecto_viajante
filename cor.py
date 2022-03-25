from cProfile import label
from math import sqrt
import numpy as raton
import math
import matplotlib.pyplot as raton
import itertools


def ciudadesdef(ciudades, viajes):
    separador_ciudades = " > "
    salto_linea = "\n"
    buffer_ciudades = []

    for viaje in viajes:
        buffer_viaje = salto_linea
        for indice_ciudad in viaje:
            buffer_viaje += separador_ciudades + ciudades[indice_ciudad]
        buffer_ciudades.append(buffer_viaje)
    return buffer_ciudades


def restastupla(tupla1, tupla2):
    return (tupla1[0] - tupla2[0])**2 + (tupla1[1] - tupla2[1])**2


# def permutations(start, end=[]):
#     if len(start) == 0:
#         print(end)
#     else:
#         for i in range(len(start)):
#             permutations(start[:i] + start[i+1:], end + start[i:i+1])
#     return permutations


ciudades = [
    "Madrid",
    "Rio",
    "New York"
]

coordenadas = [
    [0, 2, 1],
    [0, 1, 2],
    [1, 2, 0],
    [1, 0, 2],
    [2, 0, 1],
    [2, 1, 0]
]
# for coordenada in permutations(ciudades):
#     print(ciudades)



for linea in ciudadesdef(ciudades, coordenadas):
    print(linea, end=" La distancia es 88 kms ")


indices = [0, 1]
x = []
y = []
for coordenada in coordenadas:
    x.append(coordenada[0])
    y.append(coordenada[1])


# raton.scatter(coordenadas[0][0], coordenadas[0]
#               [1], color='r', label=ciudades[0])
# raton.scatter(coordenadas[1][0], coordenadas[1]
#               [1], color='b', label=ciudades[1])
# raton.scatter(coordenadas[2][0], coordenadas[2]
#               [1], color='g', label=ciudades[2])
# raton.plot(x, y, color='b')


operacion_m_ny = restastupla(coordenadas[0], coordenadas[1])
operacion_m_r = restastupla(coordenadas[0], coordenadas[2])
operacion_r_ny = restastupla(coordenadas[2], coordenadas[1])
operacion_r_m = restastupla(coordenadas[2], coordenadas[0])
operacion_ny_m = restastupla(coordenadas[1], coordenadas[0])
operacion_ny_r = restastupla(coordenadas[1], coordenadas[2])


# print(f"""Distancia de : Madrid --> New York --> Rio : {math.sqrt(operacion_m_ny) + math.sqrt(operacion_ny_r)}
# Distancia de : Madrid --> Rio --> New York : {math.sqrt(operacion_m_r) + math.sqrt(operacion_r_ny)}
# Distancia de : Rio --> New York --> Madrid : {math.sqrt(operacion_r_ny) + math.sqrt(operacion_ny_m)}
# Distancia de : Rio --> Madrid --> New York : {math.sqrt(operacion_r_ny) + math.sqrt(operacion_m_ny)}
# Distancia de : New York --> Rio --> Madrid : {math.sqrt(operacion_ny_r) + math.sqrt(operacion_r_m)}
# Distancia de : New York --> Madrid --> Rio : {math.sqrt(operacion_ny_m) + math.sqrt(operacion_m_r)}
# """)
viaje_m_r_ny = math.sqrt(operacion_m_r) + \
    math.sqrt(operacion_r_ny) + math.sqrt(operacion_ny_m)

# print(f"Total viajes dando la vuelta : {viaje_m_r_ny}")


# raton.legend()
# raton.show()
