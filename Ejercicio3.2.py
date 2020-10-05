texto=[]
def Pascal(filas):
    fila=[1]
    cero = [0]

    for i in range(filas):
        texto.append(fila)
        #print(fila)
        fila = [i + d for i, d in zip(fila + cero, cero + fila)]

    for x in reversed(texto):
        print(x)

Pascal(6)