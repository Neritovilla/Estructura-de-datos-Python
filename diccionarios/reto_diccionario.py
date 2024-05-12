lista_alumnos =[
    {"nombre":"Elena", "apellido":"De Troya","id":123,"cursos":["Fundamentos de la web", "Python"]},
    {"nombre":"Juan" , "apellido":"De Arco" ,"id":234,"cursos":["Fundamentos de la web", "Python","Mern"]},
    {"nombre":"Pedro", "apellido":"Páramo"  ,"id":345,"cursos":["Fundamentos de la web", "Python","Mern","Java"]}
]

# eliminar mern en la lista de juan
lista_alumnos[2]["cursos"].pop(2)
print(lista_alumnos)