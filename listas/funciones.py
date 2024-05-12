lista = [1, 3]

# agregar un elemento al final de la lista
lista.append(4)
print(lista)

# agregar varios elementos mediante otra lista
lista.extend([5,6,7])
print(lista)

# agregar elementos en pociciones especificas
# indice al que se desea colocar , valor (1,2)
lista.insert(1,2)
print(lista)

# eliminar datos de una lista
letras = ["x","y","z"]

# eliminar usando remove haciendo uso del valor a eliminar
letras.remove("y") # esto elimina solo la primera coincidencia q encuentra
print(letras)

# usando pop
letras.pop(1) # este metodo elimina mediante pocision y no valor
# si n oenviamos una pociosion en pop() elimina el ultimo registro

# contar el numero de ocurrencias de un valor
lista_numero = [1,2,2,1,5,1]
contador = lista_numero.count(1)
print(contador)

# obtener la pocision de un elemento mediante un valor
letras = ["x","y","z"]
posicion = letras.index("x")
print(posicion) # devuelve la posicion de la primera coincidencia


# obtener la cantidad de elementos de una lista
cantidad = len(letras)
print(cantidad)