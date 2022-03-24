from math import sqrt
import math
import matplotlib.pyplot as raton


separador_ciudades = " > "
separador_viajes = '\n'
indices = [0, 1]

coordenadas = [
    [0, 2, 1],
    [0, 1, 2],
    [1, 2, 0],
    [1, 0, 2],
    [2, 0, 1],
    [2, 1, 0]
]

ciudades = ["""
Madrid
Rio
New York
"""]

x = [60, 15, 60]
y = [25, 15, 50]


def imprime_lista(ciudades, coordenadas):
    buffer = ""
    for i_ciudad in ciudades:
        buffer = buffer + coordenadas(len[0]) - 1
    return buffer

# Calcular 
def restastupla(tupla1, tupla2):
    return (tupla1[0] - tupla2[0])**2 + (tupla1[1] - tupla2[1])**2


def linea(viaje):  # [0,1]
    buffer = ''
    for i_ciudad in viaje:
        buffer = buffer + separador_ciudades + ciudades[i_ciudad]

    return buffer


def la_lista_para_viajar(coordenadas):
    buffer = ''

    for viaje in coordenadas:
        buffer = buffer + linea(viaje) + separador_viajes
    return buffer


b = la_lista_para_viajar(coordenadas)

print(b)

operacion_m_r = restastupla(ciudades[0], ciudades[1])
operacion_r_ny = restastupla(ciudades[1], ciudades[2])
operacion_ny_m = restastupla(ciudades[2], ciudades[1])


print(f"""Distancia de : Madrid --> Rio --> New York : {math.sqrt(operacion_m_r) + math.sqrt(operacion_r_ny)} 
Distancia de : Rio --> New York --> Madrid : {math.sqrt(operacion_r_ny) + math.sqrt(operacion_ny_m)}
Distancia de : Rio --> New York --> Madrid : {math.sqrt(operacion_r_ny) + math.sqrt(operacion_ny_m)}
Distancia de : New York --> Madrid --> Rio : {math.sqrt(operacion_ny_m) + math.sqrt(operacion_m_r)}
Distancia de : New York --> Madrid --> Rio : {math.sqrt(operacion_ny_m) + math.sqrt(operacion_m_r)}
""")

viaje_m_r_ny = math.sqrt(operacion_m_r) + \
    math.sqrt(operacion_r_ny) + math.sqrt(operacion_ny_m)

print(f"Total viajes dando la vuelta : {viaje_m_r_ny}")




# primeravez = True
# for ciudad_actual in ciudades:
#     if primeravez:
#         primeravez = False
#         ciudad_anterior = ciudad_actual

#     else:
#         resta = restastupla(ciudad_anterior, ciudad_actual)


# berlin = (60, 65)
# ciudad_cabo = (10, 55)


# operacion = restastupla(madrid, berlin)
# operacion = restastupla(madrid, ciudad_cabo)

# operacion = restastupla(rio, berlin)
# operacion = restastupla(rio, ciudad_cabo)

# operacion = restastupla(new_york, berlin)
# operacion = restastupla(new_york, ciudad_cabo)
