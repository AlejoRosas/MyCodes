noCumple = []
lista = [1,2,3,4,5,6,7,8,9,10]


def saberPrimo(n):
    primo = int(n)
    cont = 0
    for i in range(1, primo + 1):
        if (primo % i) == 0:
            cont = cont + 1
    if cont == 2:
        return True
    elif cont == 0:
        return False
def noCumplen(condicion, tipo):
    length = len(lista)
    if tipo == 1:
        for i in lista:
            if i > condicion:
                noCumple.append(i)
        print(noCumple)
        del noCumple[:]
    elif tipo == 2:
        for i in lista:
            if i < condicion:
                noCumple.append(i)
        print(noCumple)
        del noCumple[:]
    elif tipo == 3:
        for i in lista:
            if saberPrimo(lista[i]) != True:
                noCumple.append(i)
        print(noCumple)
        del noCumple[:]

    elif tipo == 4:
        for i in lista:
            if saberPrimo(i) == True:
                noCumple.append(i)
        print(noCumple)
        del noCumple[:]

   # elif tipo == 5:
    #    for i in lista:
     #       if

noCumplen(5,1)

noCumplen(5,2)

noCumplen(0,4)




