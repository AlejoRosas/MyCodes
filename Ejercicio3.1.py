def saberPrimo(n):
    primo = int(n)
    cont = 0
    for i in range(1, primo+1):
        if(primo% i)==0:
            cont=cont+1
    if cont==2:
        return primo
    else:
        primo =0
        return primo


def fib2(n):
    suma=0
    result = []
    a, b = 0, 1
    while a<n:
        suma=suma+saberPrimo(a)
        result.append(a)
        a,b=b,a+b
    print(suma)
    return result

f100=fib2(100)
print(f100)