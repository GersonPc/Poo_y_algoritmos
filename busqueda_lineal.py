import random

def busqueda_lineal(lista, objetivo): # O(n)
    encontrado = False
    for elemento in lista:
        if elemento == objetivo:
            encontrado = True
            break
    return encontrado

if __name__ == "__main__":
    tamano_lista = int(input('De que tamano es la lista?: '))
    objetivo=int(input('Que numero quieres encontrar?: '))

    lista = [random.randint(0, 10) for i in range(0,  tamano_lista)]
    macht = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemto {objetivo} {"esta" if macht else "no esta"} en la lista')