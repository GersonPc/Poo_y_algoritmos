import random

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):# O(n) * O(n) = O(n * n) = O(n**2)
            if lista[j]> lista[j + 1]:
                lista[j], lista[j +1] = lista[j +1] , lista[j]
    return lista

def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
        
        lista[posicion_actual] = valor_actual

    return lista

def run():
    tamano = int(input('De que tamano quieres la lista?: '))
    lista = [random.randint(0,100) for i in range(0,tamano)]
    print(lista)
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)

if __name__ == "__main__":
    run()