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
        
 #EXERCICIO 3: VERIFICAR SE É ANO BISSEXTO  
def ano_bissexto(x):
    ano = int(x)
    
    if ano % 4 == 0 and ano % 100 != 0:
        print('Bissexto')
    elif ano % 100 == 0 and ano % 400 == 0 :
        print('Bissexto')
    else:
        print('Não Bissexto')

 #EXERCICIO 4: VERIFICAR SE É VOGAL OU CONSOANTE
def vogal_consoante(x):
    letra = x.upper()
    
    if len(letra) > 1 and letra[:1] in ('A','E','I','O','U'):
        print('Primeira letra é Vogal')
    
    elif len(letra) > 1 and letra[:1] not in ('A','E','I','O','U'):
        print('Primeira letra é Consoante')
    
    elif letra in ('A','E','I','O','U'):
        print('Vogal')
    else: 
        print('Consoante')
#EXERCICIO 5: PREÇO DO PRODUTO QUANDO ACIMA DE 10 TEM 10% DESCONTO

def preco(x):
    qtd_comprada = int(x)
    preco = 100
    
    if qtd_comprada >= 10 :
        valor_total = preco*qtd_comprada*0.9
        print(f'O valor do pedido é de R${valor_total:.2f}')
    else:
        valor_total = preco*qtd_comprada
        print(f'O valor do pedido é de R${valor_total:.2f}')
        
#EXERCICIO 6: VERIFICAR SE A PESSOA TEM MAIS DE 16 ANOS E PODE VOTAR.
def idade_voto(x):
    
    idade = int(x)
    
    if idade >= 16:
        print('Pode votar')
    else:
        print('Não pode votar')
        
def letra_numero(entrada):
    
    if entrada.isdigit() == True:
        entrada = int(entrada)
        print('É número')
        type_number(entrada)        
        par_impar(entrada)
        ano_bissexto(entrada)
        preco(entrada)
        idade_voto(entrada)
    
    else:
        print('É Letra')
        vogal_consoante(entrada)
        
entrada = input('Coloca qualquer coisa ai: ')
letra_numero(entrada)

