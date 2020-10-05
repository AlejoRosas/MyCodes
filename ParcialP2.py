#Autor: Alejandro Rosas Cuesta
#Codigo: 58231
#Descripción: Programa da solución a la petición de un programa que
# imprima los numeros divisibles por unos numeros determinados por el usuario, desde el 1 hasta el 1000

num = input("numero 1: ") # peticion del Numero 1
numDos = input("Numero 2: ") # peticion del Numero 2
numeros  = [x for x in range(1,1000) if int(x) % int(num) == 0 and int(x) % int(numDos) == 0] #Formula y lista comprimida