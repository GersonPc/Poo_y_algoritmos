import random

def busqueda_binaria(objetivo, lista, minimo, maximo):
    if minimo > maximo:
        return False
    
    mitad = (minimo + maximo) // 2

    if objetivo == lista[mitad]:
        return True
    if objetivo < lista[mitad]:
        return busqueda_binaria(objetivo, lista, minimo, mitad -1)
    else:
        return busqueda_binaria(objetivo, lista, mitad + 1, maximo)

def run():
    tamano = int(input('De que tamano quieres la lista?: '))
    objetivo = int(input('Que numero quieres encontrar?: '))

    lista = [random.randint(0,100) for i in range(0,tamano)]
    lista.sort()
    print(lista)
    encontrado = busqueda_binaria(objetivo, lista, 0, len(lista) - 1)
    print(f'El numero {objetivo} {"esta" if encontrado else "no esta"} en la lista')


if __name__ == "__main__":
    run()