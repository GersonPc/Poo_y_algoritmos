import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) //2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        print(izquierda, '*'*5, derecha)
        #Aqui se llama a la recursividad a cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        #Iteradores para recorrer las sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            print(i, izquierda, '*'*7, j, derecha)
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierza {izquierda}, derecha: {derecha}')
        print(lista)
        print('-'*30)
    return lista


def run():
    tamano = int(input('De que tamano quieres la lista?: '))
    lista = [random.randint(0,100) for i in range(0,tamano)]
    print(lista)
    print('-'*30)
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)

if __name__ == "__main__":
    run()