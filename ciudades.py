separador_ciudades = " > "
separador_viajes = '\n'
indices = [0,1]
# ciudades = ["new york", "madrid"]
# mis_viajes =[ [0,1], [1,0] ]
ciudades = ["New York", "Madrid", "Berlin", "Rio", "Ciudad Cabo"]
mis_viajes =[ [0,2,1], [0,1,2], [1,2,0], [1,0,2], [2,0,1], [2,1,0] ]

# print(ciudades[0]+ ' >> ' + ciudades[1])

# un viaj es una lista de indices de ciudades: ej [1,0,2]
def linea(viaje): # [0,1]
    buffer = ''
    for i_ciudad in viaje:
       buffer = buffer + separador_ciudades + ciudades[i_ciudad]

    return buffer


def la_lista_para_viajar(mis_viajes):
    buffer = ''

    for viaje in mis_viajes:
        buffer = buffer + linea(viaje) + separador_viajes

    return buffer


b = la_lista_para_viajar(mis_viajes)

print(b)

# b = linea([0,1])
