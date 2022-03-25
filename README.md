# Proyecto el viajante

## Preambulo

Este proyecto, llamado “El viajante” se enfrenta a que dada una lista de ciudades y la distancia entre ellas, consigamos todas las combinaciones posibles de viajes y encontremos la ruta más corta posible, pasando por cada una de las ciudades.
En este proyecto, también haremos que la pantalla nos muestre un mapa de coordenadas con las diferentes posibilidades, gracias a nuestras habilidades en programación.


## Estructura:

- Combinación de ciudades: hemos creado una variable con el listado de ciudades y otra variable con las posiciones de las ciudades. Con la ayuda de la función def hemos creado un bucle donde return buffer.
- Rutas posibles: después de obtener las combinaciones de ciudades, se ha dado valores a las rutas, se han creado las variables con tuplas de “x” e “y” con valores de coordenadas de cada ciudad y con la ayuda de los mismos bucles pero distinto código, hemos conseguido las distancias para las diferentes permutaciones.
- Mapa de coordenadas: importando la librería de matplot y dándole las variables de “x” e “y”, se ha reflejado los puntos en el mapa y con ello, los viajes.

## Problemas encontrados:

Con muchos quebraderos de cabeza, y tras una semana de trabajo en este proyecto, se ha logrado conseguir un listado de ciudades, pero sin permutaciones, en las rutas y en las distancias.
No logramos dar con el código de permutaciones, pero ha sido una buena manera de ponernos a prueba y utilizar todas las herramientas que conocemos hasta el momento.

## Estado actual: 

Actualmente el código funciona y nos refleja lo que queremos, aunque todavía no está terminado del todo.
Hemos conseguido la combinación de las cinco ciudades propuestas por nosotros, pero no hemos logrado configurar un código al que si le damos más ciudades o menos, nos haga automáticamente la combinación, por lo tanto seguimos investigando como añadir nuestro código a un bucle que logre sacar automáticamente una lista de ciudades aleatoria.
En la misma situación nos encontramos con la parte de distancias, que si le pedimos que nos refleje las distancias con las ciudades que tenemos, lo hace, pero aun no tenemos solución a si hay variaciones.
En cuanto al mapa de coordenadas, refleja perfectamente lo que queremos ver, las permutaciones de las ciudades.
