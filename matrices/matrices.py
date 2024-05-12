matriz = [
    [1,3,5,6,9],
    [3,2,4,5,8],
    [7,1,5,0,6]
]

# recorrer una matriz

for fila in matriz:
    for columna in fila:
        print(columna, end = " ")
    print()
print()
# otra manera de recorrerla usando len y los indices

for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        print(matriz[i][j], end = " ")
    print()

