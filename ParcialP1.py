#Autor: Alejandro Rosas Cuesta
#Codigo: 58231
#Descripción: El programa da solución a la petición de un código que determine
# la cantidad de veces que se repiten las letras de una lista.


#Definicion de funcion para tomar los elementos de la lista y dejarlos sin repetir
def numeroDeElementosUnicos(lista):

    unico=[]
    for x in lista:
        if x not in unico:
            unico.append(x)
    return unico
#Definición de funcion para contar los elementos de la lista
def contarElementos(unico, lista):
    numeros=[]
    tamano=len(unico)
    for i in range(0, tamano):
        numeros.append(lista.count(unico[i]))
    return numeros


lista=["A","a","m","o","n","Z","z","A","p","q","n","u"]
unica=numeroDeElementosUnicos(lista)
repeticiones=contarElementos(unica, lista)
print("Lista Completa: ", lista)
print("Lista sin repetir elementos: ",unica)
print("Cantidad de repeticiones por elemento: ",repeticiones)