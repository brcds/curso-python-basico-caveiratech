from cliente import Clientes

class Contas(Clientes):
    def __init__(self,nome, cpf, idade, limite_negativo, saldo_conta, valor):
        Clientes.__init__(self, nome, cpf, idade)
        self.limite_negativo = limite_negativo
        self.saldo_conta = saldo_conta
        self.valor = valor

    def Depositar(self, valor):
        if valor < 20:
            print('*' * 100)
            print('NÃO REALIZADO!! DEPOSITO MINIMO DE R$20 REAIS')
            print('*' * 100)
        else:
            print('*' * 100)
            print('VALOR DEPOSITADO COM SUCESSO, CONSULTA NOVO SALDO!')
            self.saldo_conta += valor
            print('*' * 100)

    def Sacar(self, valor):
        if valor > self.saldo_conta:
            print('*' * 100)
            print('IMPOSSIVEL REALIZAR SAQUE, LIMITE INDISPONIVEL\n'
                  'em caso de EMERGENCIA, SOLICITE O CREDITO ESPECIAL!!!')
            print('*' * 100)
        else:
            print('*' * 100)
            print('OK! SAQUE REALIZADO COM SUCESSO')
            self.saldo_conta -= valor
            print('*' * 100)

    def Saldo(self, cpf):
        print('*' * 100)
        print('NOME: {}\nCPF: {}\nSALDO: {}'.format(self.nome, self.cpf, self.saldo_conta))
        print('*' * 100)

    def CreditoEspecial(self, valor):
        if valor > 1000:
            print('*' * 100)
            print('SEU CREDITO ESPECIAL É DE 1000,\nCASO PRECISE DE UM NOVO VALOR\n'
                  'SOLICITE JUNTO AO SEU GERENTE.')
            print('*' * 100)
        else:
            print('*' * 100)
            print('OK, PRONTINHO!! ESSE VALOR FICARA NEGATIVADO EM SUA CONTA\n'
                  'ATÉ QUE SEJA QUITADO, AGRADECEMOS A PREFERENCIA E FICAMOS\n'
                  'FELIZES EM PODER AJUDAR.')
            self.saldo_conta -= valor
            print('*' * 100)
