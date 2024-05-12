# decalarar set, los valores no se pueden repetir, en caso que lo haga no lo agrega al valor repetido
# no poseen orden ni indice

set1 = {2,3,5,7}
set2 = set([2,3,5,7])

nombres = {"Elena","Juana","Pablo"}

# recorrerlo
for nombre in nombres:
    print(nombre)

# verificar si existe un valor en el set
existencia =  "Elena" in nombres
print(existencia)

# agregar elementos
nombres.add("Pedro")
print(nombres)

# eliminar un elemento
nombres.remove("Elena")
print(nombres)

#eliminar un elemento al azar
nombres.pop()
print(nombres)