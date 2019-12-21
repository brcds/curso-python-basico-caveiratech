minha_lista = ['bruno', 'bea']  #LISTA (LIST)
minha_tupla = ('bruno', 'bea')  #TUPLA (TUPLE)
meu_dicionario = {'nome': 'BrunoCristiano', 'idade': 21} #DICIONARIO (dict)
meu_conjunto = {'bruno', 'bea'} # CONJUNTO (set)

print(type(minha_tupla))

print(minha_tupla[1])
print('*' * 50)

for nomes in minha_tupla:
    print(nomes)

print('*' * 50)

if 'bruno' in minha_tupla: # consigo realizar essa pesquisa com todas coleçoes (menos dicionario)
    print('bruno esta na tupla')

print('*' * 50)

print(meu_dicionario)

print(meu_dicionario['nome'])
print(len(meu_dicionario)) # len funciona com todas as coleçoes

print('*' * 50)

if 'BrunoCristiano' in meu_dicionario.values():
    print('bruno esta no dicionario')

for valores in meu_dicionario.values():
    print(valores)

for chaves in meu_dicionario.keys():
    print(chaves)

meu_dicionario['nome'] = 'joao'
meu_dicionario['idade'] = '25'
meu_dicionario['endereco'] = 'AV. ze lira'
meu_dicionario['telefone'] = '987582949'
print(meu_dicionario)

print('*' * 50)
print('\n')

meu_conjunto.add('maria')
meu_conjunto.add('bruno')

if 'bruno' in meu_conjunto:
    print('ENCONTRADO')
print(meu_conjunto)

''' O CONJUNTO É O MAIS UTILIZADO PARA PESQUISAS,
POIS UTILIZA UMA TABELA HASH COMO PESQUISA '''

print('*' * 50)
print('\n')

''' INICIANDO AS COLEÇOES '''

lista = []
tupla = ()
dicionario = {}
conjunto = set()

''' Cada coleção poderá ser usada dependendo da situação.
'''