
lista = [2,7,85,45,3]

# Sumatoria d euna lista
suma = 0
for num in lista:
    suma += num

print(suma)

# promedio de una lista
promedio = 0

for num in lista:
    promedio += num

promedio = promedio/len(lista)
print(promedio)

# obtener el maximo y min de una lista

# maximo
max = lista[0]
for num in lista:
    if max < num:
        max = num
print(f'maximo: {max}')

# minimo
min = lista[0]
for num in lista:
    if min > num:
        min = num
print(f'minimo: {min}')