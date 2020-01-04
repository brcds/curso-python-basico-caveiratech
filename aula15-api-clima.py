import requests
import json

clima = None
cidade = input('VERIFICAR CLIMA\nINFORME A CIDADE: ')
req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                   +cidade+'&appid=876b7f491eb1f01e8856c900972dbc15')

clima = json.loads(req.text)
print('Condição do tempo: ', clima['weather'][0]['main']) #usar api do google p traduzir
print('temperatura: {:.02f}'.format(float(clima['main']['temp'] - 273.15)))
#print('Temperatura: ', float(clima['main']['temp'] - 273.15))
