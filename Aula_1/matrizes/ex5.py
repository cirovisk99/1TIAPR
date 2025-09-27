'''Multiplicacão de matrizes
Crie uma matriz 2x3 e uma 3x2 e calcule o produto das duas matrizes
'''

def produto(matriz_1,matriz_2):
    matriz_produto = [[0 for _ in range(len(matriz_2[0]))] for _ in range(len(matriz_1))]
    
    for i in range(len(matriz_1)): # Cria cada linha da matriz resultado, ou seja, a quantidade de linhas da matriz 1
        for j in range(len(matriz_2[0])): # Calcula cada célula da matriz resultado com a soma das multiplicações, ou seja, a quantidade de colunas da matriz 2
            for k in range(len(matriz_1[0])):    # faz cada multiplicação , ou seja a quantidade de linhas da matriz_1
                matriz_produto[i][j] = matriz_produto[i][j] + (matriz_1[i][k]*matriz_2[k][j])
        
    return matriz_produto
    
matriz_1 = [
    [1,2,3],
    [4,5,6]
]    

matriz_2 = [
    [4,5],
    [6,7],
    [8,9]
]

resultado = produto(matriz_1,matriz_2)
print(resultado)