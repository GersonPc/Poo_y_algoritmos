import time

def factorial(numero):
    respuestas = 1
    while numero > 1:
        respuestas *= numero 
        numero -= 1
    
    return respuestas

def factorial_r(numero):
    if numero == 1:
        return 1
    return numero * factorial_r(numero - 1)

if __name__ == "__main__":
    numero = int(input('Escribe el numero para factorializarlo :v : '))
    comienzo = time.time()
    print(factorial(numero))
    final = time.time()
    print(final - comienzo)