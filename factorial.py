def factorial(valor):
    if valor == 1:
        return 1
    
    return valor * factorial(valor -1)

if __name__ == "__main__":
    valor = int(input('Pon un numero para sacar el factoial: '))
    res = factorial(valor)
    print(res)