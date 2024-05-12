directorio_direccions = {
    "Elena" : "Roma 123, Italia",
    "Juana" : "Paris 22A, Francia",
    "Pablo" : "Malaga 89, España",
}

# encontrar la llave respecto a un valor

direccion_buscar = "Paris 22A, Francia"

if(direccion_buscar in directorio_direccions.values()):
    for persona, direccion in directorio_direccions.items():
        if(direccion_buscar == direccion):
            print(persona)
else:
        print("No existe la dirección indicada")

