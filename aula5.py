## for and whille

lista_nomes = ['bruno', 'bea', 'magal', 'polly']

# print(lista_nomes)
# print(lista_nomes[0])

for i in range(len(lista_nomes)):
    print(lista_nomes[i])
    lista_nomes.append('OII')

print(lista_nomes)

"""for nomes in lista_nomes:
    print(nomes)"""

"""for i in range(5):
   print(lista_nomes[i])"""
i = 0

while i < 10:
    print('i ainda é menor que 10: ', i)
    i = i + 1

frutas = ['abacaxi','maca','banana','melancia']

contador = 0

for item in frutas:
    contador += 1
print(contador)
print('*' * 50)

print(len(frutas))
print('*' * 50)

numero = 0
while True:
    print(numero)
    if numero == 20:
        print('FIM')
        break
    numero += 1

print('*' * 50)



