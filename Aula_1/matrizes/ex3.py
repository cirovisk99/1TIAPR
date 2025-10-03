''''Matriz transposta'''

def transposta(matriz):
    
    matriz_transposta = []
    
    for i in range(len(matriz[0])): 
        linha = [] 
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        matriz_transposta.append(linha)
        
    return matriz_transposta

matriz = [
    [1,2],
    [3,4],
    [5,6]
]

resultado = transposta(matriz)

print(resultado)
