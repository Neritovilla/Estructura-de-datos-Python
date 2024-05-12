# es una estructura de datos para almacenar informacion, son dinamicas y mutables
lista = ["a","b","c"]

# las listas pueden ser de un mismo tipo o poseer diferentes tipos de datos
lista_dos = ["a", 1, 20.5, ["a","b"]]

# cada elemento tiene una pocision dentro de la lista
#         0   1   2
lista = ["a","b","c"]

# podemos acceder al elemento mediante su pocision
print(lista[1])

#modificar un valor por poocision
lista[1] = "f"
print(lista)

# obtener  un numero fijo de valores de la lista, generando una nueva sublista
lista_nueva = lista[0:1]
print(lista_nueva)

# modificar varios valores a la vez
lista[1:3] = ["w","z"]
print(lista)