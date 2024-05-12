# similares  alas listas, pero estas no pueden ser modificadas

# como declarar tuplas
tupla = ("a","b","c")
tupla_dos = 1,2,3,4

# convertir tupla en lista usando list()
tupla_original = ("a","b","x")
lista = list(tupla_original)
print(lista)

# convertir lista a tupla
lista_original = [1,2,3]
nueva_lista = tuple(lista_original)
print(nueva_lista)

# recorrer una tupla
tupla_letras = ("x","y","z")
for letra in tupla_letras:
    print(letra)
print()