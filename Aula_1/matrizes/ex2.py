'''Multiplicação escalar'''

def escalar(matriz, fator):
    
    matriz_multi = []
    
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j]*fator)
        matriz_multi.append(linha)
    return matriz_multi

matriz = [
    [1,2],
    [3,4]
    ]

fator = 2

resultado = escalar(matriz,fator)
print(resultado)
