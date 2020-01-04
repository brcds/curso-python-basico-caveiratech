#entrada e saida de arquivos

'''
METODOS OPEN RECEBE DOIS ARGUMENTOS -.
OPEN(NOME DO ARQUIVO, OUTROMETODO)
    SE COLOCAR SOMENTE UM ARGUMENTO ELE USA O 'a' DE READ, CASO NAO EXISTA ELE DA PAU
    O METODO 'w' ELE CRIA O ARQUIVO CASO NAO EXISTA, SE EXISTI ELE SOBRESCREVE
    O METODO 'r+' metodo de leitura e escrita.
    O METODO 'a' de append, metodo de escrita com append, ele nao sobrescreve
        nem apaga, ele adiciona ao arquivo.
        #TODO ARQUIVO QUE NAO SEJA DE TEXTO VOCE USA O METODO 'b' de bits.'''

arquivo = open('arquivo.txt', 'r')

'''for i in range(0, 1000):
    arquivo.write('aaaa '+ str(i) +'\n') #write é funcao escrever.'''

'''print(arquivo.read())
print(arquivo.write())

for linha in arquivo:
    print(linha)'''
