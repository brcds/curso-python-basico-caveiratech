#api e requisicoes web

import requests
import json
req = None
e = None

def requisicaoendereco(cep):
    try:
        req = requests.get('http://viacep.com.br/ws/' + cep +'/json/' )
        dicionario = json.loads(req.text)

        return dicionario
    except Exception as e:
        print('ERRO NA CONEXÃO')
        return e

def mostrarendereco(cep):
    print('CEP: ', endereco['cep'])
    print('ENDERECO: ', endereco['logradouro']),
    print('COMPLEMENTO: ',endereco['complemento'])
    print('BAIRRO: ', endereco['bairro'])
    print('LOCALIDADE: ',endereco['localidade'])
    print('ESTADO: ',endereco['uf'])

sair = False
while not sair:
    cep = input('informe seu cep ou SAIR para fechar! ')
    if cep == 'SAIR':
        sair =True
    else:
      endereco = requisicaoendereco(cep)
      print(mostrarendereco(cep))
      '''if endereco['erro'] == True:
          print('erro')
      else:
        '''


