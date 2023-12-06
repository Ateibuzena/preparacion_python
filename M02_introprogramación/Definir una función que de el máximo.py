# Definir una fnción que tome dos números y devuelva el mayor de ellos.

def max (n1,n2):
    if n1>n2:
        print("El número mayor es:", n1)
    elif n1==n2:
        print("Los dos números son iguales")
    else:
        print("El número mayor es:", n2)

n1 = float(input("Ingrese un número:"))
n2 = float(input("Ingrese otro número:"))

print (max(n1,n2))


