import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    if comienzo > final:
        return False

    mid = (comienzo + final) // 2
    
    if  lista[mid] == objetivo:
        return True
    elif lista[mid] > objetivo:
        return busqueda_binaria(lista, comienzo, mid -1, objetivo)
    else:
        return busqueda_binaria(lista, mid + 1, final, objetivo)

if __name__ == "__main__":
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range (tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemto {objetivo} {"esta" if encontrado else "no esta"} en la lista')