from cliente import Clientes
from contas import Contas

cliente1 = Clientes('Bruno Cristiano', 11912026406, 21)
conta1 = Contas(cliente1.nome, cliente1.cpf, cliente1.idade, 0, 0, 0)

rodadas = 1
servicos = 1

def nova_operacao(new):
    if new == 'sim':
        return True
    elif new == 'nao':
        return False
    else:
       return print('OPCAO INVALIDA, REINICIE SEU PROCESSO')

while rodadas >= servicos:
    opcao = int(input('\n** BEM VINDO AO SEU CAIXA RAPIDO **\n\n'
                      '1 -> SACAR **\n'
                      '2 -> DEPOSITAR **\n'
                      '3 -> CREDITO ESPECIAL **\n'
                      '4 -> SALDO **\n'
                      '\nINFORME A OPCAO DESEJADA: '))

    if opcao == 1:
        sacar = int(input('\nINFORME O VALOR DO SAQUE R$: '))
        conta1.Sacar(sacar)
        new = input('\nDeseja fazer outra operacao?\nRESPONDA -> SIM OU NÃO\n ->')

        if nova_operacao(new) == True:
            rodadas += 1
        elif nova_operacao(new) == False:
            print('\n\n AGRADECEMOS A PREFERENCIA :) ')
            rodadas = 0
        else:
            print(nova_operacao(new))

    elif opcao == 2:
        depositar = int(input('INFORME O VALOR DO DEPOSITO R$: '))
        conta1.Depositar(depositar)
        new = input('\nDeseja fazer outra operacao?\nRESPONDA -> SIM OU NÃO\n ->')

        if nova_operacao(new) == True:
            rodadas += 1
        elif nova_operacao(new) == False:
            rodadas = 0
        else:
            print(nova_operacao(new))

    elif opcao == 3:
        saqueespecial = int(input('INFORME O VALOR DE SAQUE ESPECIAL R$: '))
        conta1.CreditoEspecial(saqueespecial)

        new = input('\nDeseja fazer outra operacao?\nRESPONDA -> SIM OU NÃO\n ->')

        if nova_operacao(new) == True:
            rodadas += 1
        elif nova_operacao(new) == False:
            rodadas = 0
        else:
            print(nova_operacao(new))

    elif opcao == 4:
        saldo = int(input('INFORME SEU CPF, PARA CONSULTAR O SEU SALDO -> '))
        conta1.Saldo(saldo)

        new = input('\nDeseja fazer outra operacao?\nRESPONDA -> SIM OU NÃO\n ->')

        if nova_operacao(new) == True:
            rodadas += 1
        elif nova_operacao(new) == False:
            rodadas = 0
        else:
            print(nova_operacao(new))

    else:
        print('*' * 50)
        print('ERRO! ' * 5)
        print('-' * 50)


