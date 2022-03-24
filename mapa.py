# Problema del viajante ¿Cuál es el viaje más efectivo?
# Factorial por cada ciudad que se añade
# 3 ejercicios
# Ciudades: Madrid(50,60) Berlin(60,65) New York(25, 60) Rio de Janeiro(15, 15) Ciudad del Cabo(55, 10)
# Distancias
# Mapa

import matplotlib.pyplot as raton
x = [60, 15, 60]
y = [25, 15, 50]

raton.scatter(x, y, color='r',zorder=2)
raton.plot(x, y, color='b',zorder=1)


# new_york = raton.plot(x, y, marker="o", color="red", label="New York")
# rio = raton.plot(x, y, marker="o", color="blue", label="Rio")
# madrid = raton.plot(x, y, marker="o", color="green", label="Madrid")
# # berlin = raton.plot(65, 60, marker="o", color="y", label="Berlin")
# # ciudad_cabo = raton.plot(10, 55, marker="o", color="m", label="Ciudad Cabo")


raton.legend()
raton.show()
