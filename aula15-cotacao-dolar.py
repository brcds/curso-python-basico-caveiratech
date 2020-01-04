#cotacao do dolar

import requests
import json
import time
import datetime

while True:
    requisicao = requests.get(' https://economia.awesomeapi.com.br/all')
    cotacao = json.loads(requisicao.text)
    print('### COTACOES ###', datetime.datetime.now())
    print('DOLAR: ',cotacao['USD'] ['high'])
    print('EUROS: ',cotacao['EUR']['high'])
    print('BITCOIN: ',cotacao['BTC']['high'])
    time.sleep(2)


