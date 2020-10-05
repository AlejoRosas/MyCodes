listConcepto = []
listDefinicion = []
def sum(a,b):
    for n in (a,b):
        if not isinstance(n, int) and not isinstance(n,float):
            raise TypeError
        return a+b
def agregarTiempo(a):
    if a<1:
        raise TypeError
    else:
        a = True
        return a
def guardarConcepto(concepto):
    if not isinstance(concepto, str):
        return False
    else:
        listConcepto.append(concepto)
       # print(listConcepto)
        return "Guardado exitoso"

def guardarDefinicion(definicion):
    if not isinstance(definicion, str):
        return False
    else:
        return "Guardado Exitoso"

def buscarConcepto(concepto):
    for i in listConcepto:
        print(i)
        if i == concepto:
            return True
        else:
            return False

def buscarDefinicion(concepto):
    for i in listConcepto:
        print(i)
        if i == concepto:
            return True
        else:
            return False