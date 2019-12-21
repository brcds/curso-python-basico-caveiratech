from select import error

import requests #beautiful Soup 4 BS4 pip install bs4
from requests.cookies import merge_cookies

err = 'x'
cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com'}

meuscookies = {'Ultima-visita': '10/10/2020'}
dados = {'username': 'brunao',
         'password': 'brunao123'}

texto = None

try:
    requisicao = requests.post('https://putsreq.com/0eUBCXDjZl4ae0h7fcR9',
                                headers=cabecalho,
                                cookies=meuscookies,
                                data=dados)
    texto = requisicao.text
except Exception as err:
    print('Requisicao deu ERRO! ')
    print(err)


#print(type(requisicao))
print(texto)

