# Definir una función que recorra una palabra dada y 
# te diga que letra hay en la posición 3

palabra = str(input("Escribe una palabra terminada en punto:"))

def rec_palabra(palabra):
    return (palabra[2])


print (rec_palabra(palabra))