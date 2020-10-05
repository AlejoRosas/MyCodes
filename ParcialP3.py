#Autor: Alejandro Rosas Cuesta
#Codigo: 58231
#Descripción: El programa no da la solucion al imprimir pares de las palabras con mas letras en comun, sin repetir palabras.
#En cambio el programa muestra las letras en común de todas las palabras entre ellas y
# las imprime en orden de mayor a menor cantidad de letras en común
lista = ["decir","balneario","habria","cabria","seria","abanico","quesera","mentir"]
listaComparadas =  []
def contarLetras(palabra, palabra2):
    contador = 0
    bloque = []
    listaLetras = []
    listaLetras2 = []
    listaRespaldo  = []

    for x in range(len(palabra)):
        listaLetras.append(palabra[x])
    for y in range(len(palabra2)):
        listaLetras2.append(palabra2[y])
    for a in range(len(palabra)):
        for b in range(len(palabra2)):
            if listaLetras[a] == listaLetras2[b]:
                if listaLetras2[b] not in listaRespaldo:
                    listaRespaldo.append(listaLetras2[b])
                    contador += 1
                break
    bloque = contador, palabra, palabra2
    if contador not in listaComparadas:
        listaComparadas.append(bloque)

    return contador, palabra, palabra2
def ordenarEimprimir():
    listaComparadas.sort()
    listaComparadas.reverse()
    print(listaComparadas)

for x in range(len(lista)):
    for y in range(len(lista)):
        if lista[x]!=lista[y]:
           contarLetras(lista[x], lista[y])

ordenarEimprimir()







