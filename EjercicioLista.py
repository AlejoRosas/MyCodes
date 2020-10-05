numeros = [2,5,2,1,1,5,8,2,3]
aux = []
estado = False
for x in range(0,len(numeros)):
    for y in range(0,len(aux)):
        if len(aux)==0:
            aux[0] = numeros[0]
        elif numeros[x] == aux[y]:
            estado= True
            break
    if estado == False:
        aux.append(numeros[x])
    estado = False
print(aux)