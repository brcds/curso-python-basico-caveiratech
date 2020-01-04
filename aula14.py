#expressoes-regulares
import re
#regex101.com
teste = 'O gato é bonito, a gata, os gatinhos, os gatoes'
padrao = re.findall(r'gat\w*', teste)

if padrao:
    print(padrao)
else:
    print('padrao nao ENCONTRADO')

