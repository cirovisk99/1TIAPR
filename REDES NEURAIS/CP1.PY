'''CHECKPOINT 1 - REDES NEURAIS'''

'''VARIÁVEIS INICIAIS'''
X1 = [0.5 , 0.2]
X2 = [0.8 , 0.4]
Y = [1 , 0]

W1= 0.2
W2 = -0.1

taxa_aprendizado = 0.1

erro = 0

acuracia = 0
acuracidade = 1

epoca = 1
while epoca <= 15:

    for i in range(len(X1)):
        soma = X1[i]*W1 + X2[i]
        if soma >= 0:
            degrau = 1
        else:
            degrau = 0
        
        erro_x = Y[i] - degrau
        acuracia = acuracia + erro
        
        if erro_x == 0:
            pass
        else:
            X_1 = X1[i]
            X_2 = X2[i]
            erro = erro_x
        
    
    acuracidade = acuracia/2
    epoca = epoca + 1 
    
    print(X_1,X_2)
    
    W1 = W1 + taxa_aprendizado*erro*X_1
    W2 = W2 + taxa_aprendizado*erro*X_2
    
    print(f'W1: {W1:.2f}  e W2: {W2:.2f} \n Epoca {epoca} \n % ACC: {acuracidade} \n erro:{erro}' )



    
    
    
        
        
