salada = True

b = 0
x = '12' #  <= quantidade de vezes que vai repetir a pergunta ...

print('*' * 50)
print('BEM VINDO AO GAMESALADA, ACERTE AS DUAS PERGUNTA'
      '\nJUNTE PONTOS E PASSE PARA A PROXIMA FASE!!')
print('*' * 50)

for ingredientes in x:
    a = input('cite os dois principais ingrediente da salada ? ')
    if a == 'tomate':
        print('ok!z\n UM TOMATE É ESSENCIAL\nGanhou 1 ponto, FALTA SO +1')
        print('+' * 50)
        b = (b + 1)
        x = '12'
    elif a == 'alface':
        print('ok!\n UM ALFACE É ESSENCIAL\nGanhou 1 ponto, FALTA SO +1')
        print('+' * 50)
        b = (b + 1)
        x = '12'
    else:
        print('isso não é para salada ')
        print('-' * 50)
        b = (b - 1)

if b >= 2:
    print('sua pontuacao {},\n voce VENCEU'.format(b))
    print('*\n' * 2)
else:
    print('voce PERDEU\n SUA PONTUACAO {}'.format(b))


