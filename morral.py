
def morral(tamano_morral, pesos, valores,n):
    print(f'Tamano de Morral: {tamano_morral}, pesos: {pesos}, valores: {valores}, n: {n}')
    if n==0 or tamano_morral == 0:
        return 0
    
    if pesos[n-1] > tamano_morral:
        return morral(tamano_morral, pesos,valores,n-1)
    print('-'*20)
    print(f'Tamano de Morral: {tamano_morral}, pesos: {pesos}, valores: {valores}, n: {n}')
    return max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos,valores,n-1),
                morral(tamano_morral,pesos,valores, n-1))

if __name__ == "__main__":
    valores = [50, 70, 90]
    pesos = [10, 20,30]
    tamano_morral = 40
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)