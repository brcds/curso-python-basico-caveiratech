from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6,'ford', 10)

#print(caminhao_rosa)
#print(type(caminhao_rosa))

print('\ncarro rosa')
print('cor: {} \nrodas: {} \nmarca: {} \ntanque: {} \n'.format(caminhao_rosa.cor,caminhao_rosa.rodas,
                                                             caminhao_rosa.marca, caminhao_rosa.tanque))
print('carro azul')
carro_azul = Carro ('azul', 'bmw', 7)
print('cor: {} \nrodas: {} \nmarca: {} \ntanque: {} \n'.format(carro_azul.cor,carro_azul.rodas,
                                                             carro_azul.marca, carro_azul.tanque))
carro_azul.abastecer(5000)
caminhao_rosa.abastecer(100)

print(caminhao_rosa.tanque)

print(carro_azul.tanque)
