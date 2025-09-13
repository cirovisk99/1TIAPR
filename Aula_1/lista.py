print('Exercício soma da lista de numeros')
lista_numeros = [1,2,3,4,5]

#soma = lista_numeros[0] + lista_numeros[1] + lista_numeros[2]  + lista_numeros[3] + lista_numeros[4] 
soma = sum(lista_numeros)

print(lista_numeros)
print(f'A soma da lista é {soma}')

print('\nExercício lista com 3 strings e concatenar')
lista_string = ['Hello' , 'World' ,'Olá', 'Mundo' ]

frase = ','.join(lista_string)
print(lista_string)
print(f'A frase é {frase}')

print('\nLista com 4 numeros e encontre o maior e o menor número da lista')
numeros = [10, 25, 30, 15, 5]

maior_numero = max(numeros)
menor_numero = min(numeros)

##maior_numero = lista_numeros[len(lista_numeros)]
print(numeros)
print(f'O maior número é {maior_numero} e o menor número é {menor_numero}.')

print('\n lista com 5 nomes e verifique se um nome especifico esta na lista')
nomes = ['ciro' , 'floki' , 'brookie' , 'nathalia']
nome = 'clovis'
print(nome)
encontrou_nome = nome in nomes

if encontrou_nome == True:
    print('Encontrou')
    
else:
    print('Não encontrou')
    
print('\n lista com 6 números e faz a media')
numeros = [10, 25, 30, 15, 5]
media = sum(numeros)/len(numeros)
print(numeros)
print(f'A média é {media}')
