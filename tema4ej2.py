mi_lista = [3, 4, 8, 5, 5, 22, 13]

def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

primos = list(filter(es_primo, mi_lista))


print(primos)