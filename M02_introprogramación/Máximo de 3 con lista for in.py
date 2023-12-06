# Definir una función "máximo de tres"
# Que tome tres números y te de el mayor

n1 = float(input("n1 = "))
n2 = float(input("n2 = "))
n3 = float(input("n3 = "))

def max_3 (n1, n2, n3):
    nmax = n1
    lista = [n1, n2, n3]
    for n in lista:
        if n > nmax:
            nmax = n
    return (nmax)

print(max_3(n1, n2, n3))


