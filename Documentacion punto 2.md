
# Documentacion Punto 2


La forma en la que solucione el problema  fue utilizando  la estadistica , creando un diccionario de listas
con el caracter y  las posiciones en las que aparece en cada log , posteriormente  halle la posicion  media de cada caracter 
sumando la suma de las posiciones  y dividiendolo por la cantidad de apariciones ,  posteriormente ordeno el diccionario por valor,
de modo que los caracteres con una posición media menor aparezcan antes que los que tienen una posición media mayor.
Por último, concatenamos los caracteres ordenados y devolvemos el resultado


# Funciones


# create_dict_of_login

esta  funcion se encarga de crear un diccionario con  los caracteres y su posicion dentro de los grupos de tres , guardandolo en diccionarios de listas.
donde la clave es el caracter y el valor es la lista con las apariciones del caracter.

# Find_position

esta  función  se encarga de  calcular la posición media  de cada carácter  dividiendo  la suma de las posiciones del carácter por el número de veces que ha aparecido el carácter.

# fin_the_password

esta  función  se encarga de ordenar  el diccionario por valor, de modo que los caracteres con una posición media menor aparezcan antes que los que tienen una posición media mayor.
Por último, concatenamos los caracteres ordenados y devolvemos el resultado.


