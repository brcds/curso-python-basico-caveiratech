# funçoes e metodos

def soma(numero1, numero2):
    resp = numero1 + numero2
    return resp

resultado = soma(75, 1289) #possivel realizar essa soma com numero floats.
print(resultado)

print('*' * 50)
print('\n')

def imprimi_oi(): #em uma funcao nao è obrigatorio ter parametros de entrada ou saida.
    print('oi')

imprimi_oi()

print('*' * 50)
print('\n')

def tem_sete_letras(objeto):
    if len(objeto) == 7:
        return True
    else:
        return False

if tem_sete_letras('1234567'):
    print('tem sete letras')
else:
    print('não tem sete letras')



