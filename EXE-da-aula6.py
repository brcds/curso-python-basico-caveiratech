'''
    ESCREVA UMA FUNCAO QUE RECEBA UM OBJETO DE COLEÇÃO, E RETORNA O VALOR DO MAIOR NUMERO
    DENTRO DESSA COLEÇÃO, FAÇA OUTRA FUNCAO QUE RETORNE O MENOR NUMERO DESSA COLEÇÃO
'''
def retorna_maior_valor(valores):
    return max(valores)

def retorna_menor_valor(valores):
    return min(valores)

minha_lista = []
rodadas = 0
posicoes = int(input('informe o numero de pocisoes da lista: '))

while rodadas < posicoes:
    numero = int(input('informe os valores: '))
    minha_lista.append(numero)
    rodadas += 1

print('esses são os valores da sua lista: {} '.format(minha_lista))
print('esse é o maior valor da sua lista: {}'.format(retorna_maior_valor(minha_lista)))
print('esse é o menor valor da sua lista: {}'.format(retorna_menor_valor(minha_lista)))

