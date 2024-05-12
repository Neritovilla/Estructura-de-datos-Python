lenguajes1 ={"Python", "C++", "Java"}
lenguajes2 ={"Cobolt", "Java", "C#"}

# unir sets
lenguajes = lenguajes1.union(lenguajes2)
print(lenguajes)

# interseccion ---- muestra todos los valores en coun entre sets
concidencias = lenguajes1.intersection(lenguajes2)
print(concidencias)

# verificar que no exista coincidencias entre sets
noExisteCoincidencias = lenguajes1.isdisjoint(lenguajes2) # devuelve un true o false
print(noExisteCoincidencias)

# elimina concidencias entre set 1 y 2 , y devuelve los valores del set 1 sin la coincidencia con el set 2
diferencias = lenguajes1.difference(lenguajes2)
print(diferencias)