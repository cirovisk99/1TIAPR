#LISTA 3 EXERCICIOS
#EXERCICIO 1: PROGRAMA QUE IDENTIFICA QUE O NÚMERO É POSITIVO, NEGATIVO OU ZERO
def type_number(x) :
    numero = int(x)
    
    if numero > 0:
        print('Positivo')
    elif numero <0:
        print('Negativo')
    else:
        print('Zero')
 
 #EXERCICIO 2: VERIFICAR SE É PAR OU ÍMPAR
 
def par_impar(x) :
    numero = int(x)
    
    if round(numero/2,0) == numero/2:
        print('Par')
    else:
        print('Ímpar')      
    



 
numero = input('coloca um numero ai: ')
type_number(numero)        
par_impar(numero)

