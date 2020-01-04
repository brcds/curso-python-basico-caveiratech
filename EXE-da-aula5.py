'''FAÇA UM PROGRAMA QUE LEIA A QUANTIDADE DE PESSOAS QUE
SERÃO CONVIDADAS PARA UM FESTA.
    APÓS ISSO O PROGRAMA IRA PERGUNTAR O NOME DE TODAS AS PESSOAS E COLOCAR EM UMA LISTA
    DE CONVIDADOS
APOS ISSO, IRA IMPRIMIR TODOS OS NOMES DA LISTA'''

lista_convidados = []
num_convidados = (len(lista_convidados))

num_convites = int(input('Quantos convites disponiveis? '))
print('*' * 50)

while num_convidados < num_convites:
    pessoa_convidada = input('INFORME O NOME DO CONVIDADO: ')
    lista_convidados.append(pessoa_convidada)
    num_convidados += 1
    print('TOTAL DE CONVIDADOS {}'.format(num_convidados))
    print('TOTAL DE CONVITES {} '.format(num_convites))
    print('*' * 50)

for pessoas in lista_convidados:
    print('CONVIDADO: {} '.format(pessoas))


