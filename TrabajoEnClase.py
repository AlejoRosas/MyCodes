def es_primo(num):
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return True
    return True    #de lo contrario devuelve Verdadero

def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        fibo.append(a)

    #print()
fibo = []
primos = list(filter(es_primo, fibo))

fib(1000)

print(fibo)