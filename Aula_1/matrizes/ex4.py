'''Verificar se é matriz identidade
Matriz identidade é uma matriz quadrada que que todos os elementos da diagonal principal sao iguais a 1 e os outros elementos iguais a zero.

'''
def identidade(matriz):
    
    flag = True
    if range(len(matriz)) == range(len(matriz[0])):
    
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if i ==j and matriz[i][j] == 1:
                    pass
                elif matriz[i][j] == 0:
                    pass
                else:
                    flag = False
                    break
            
        if flag == True:
            result = 'É Identidade'
        else:
            result = 'Não é identidade'
    else:
        result = 'Não é identidade pois não é quadrada'
        flag = False
        
    return result

matriz = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]

resultado = identidade(matriz)

print(resultado)
    