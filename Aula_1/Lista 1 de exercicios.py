nome = "Ciro Junichi Yamauchi"
idade = 26 
cidade = "São Paulo"
carro = True
percentual = 10/3

if carro == True:
    carro_string = 'Tem carro'
else:
    carro_string = 'Não tem carro'

print(f'Seu nome é {nome},\nVocê tem {idade} anos e mora na cidade de {cidade},\n{carro_string} e tem o percentual de {round(percentual,2)}%.')


'''Desafio: Trocar variáveis de lugar Ex: Idade virar o nome e o nome virar a idade'''
'''Forma batata de fazer'''
nome_2 = nome
nome = idade
idade = nome_2

print(f'\n\nSeu nome é {nome} e sua idade é {idade}')

'''Forma certa de fazer'''

idade , nome = nome, idade

print(f'\n\nSeu nome é {nome} e sua idade é {idade}')
