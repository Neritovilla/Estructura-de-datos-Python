
lista =["g","f","e","d","c","b","a"]

# recorrer una lista a la inversa
nueva_lista =[]
for indice in range(len(lista)-1, -1, -1):
    nueva_lista.append(lista[indice])
print(nueva_lista)

# usando reversed()
nueva_lista =[]
for letra in reversed(lista):
    nueva_lista.append(letra)
print(nueva_lista)

# otra forma de usar reversed()
nueva_lista =[]
nueva_lista = lista
nueva_lista.reverse()
print(nueva_lista)

# o de la siguiente manera
lista =["g","f","e","d","c","b","a"]
print(lista[::-1])