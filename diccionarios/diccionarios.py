# estructura de datos que permiten guardar valores, mediante llaves y valores

# estructura
estudiantes = {
    "nombre" : "erick",
    "apellido" : "villavicencio",
    "edad" : 26
}

# acceder a un valor
nombre = estudiantes["nombre"]
print(nombre)

#modificar valores
estudiantes["nombre"] = "rodrigo"
print(estudiantes)

# agregar nuevos valores
ciudad = 'quito'
estudiantes["ciudad"] = ciudad
print(estudiantes)
print()

# recorrer el diccionario
for llave in estudiantes:
    print(estudiantes[llave])
print()