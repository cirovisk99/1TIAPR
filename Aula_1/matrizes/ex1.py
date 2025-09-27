'''Crie duas matrizes 3x3 e calcule a soma delas'''
def soma_matriz(matriz1, matriz2):

    matriz_soma = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j] + matriz2[i][j])
        matriz_soma.append(linha)
    
    return matriz_soma

matriz1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

matriz2 = [
    [11,12,13],
    [14,15,16],
    [17,18,19]
    ]

resultado = soma_matriz(matriz1 , matriz2)
print(resultado)
