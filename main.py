from banco import *
from operacoes.transferencia import transferir
from operacoes.saque import sacar
from operacoes.consulta import consultaSaldo
from operacoes.deposito import depositar

def menu():
    while True:
        print("------ BEM VINDO AO BASIC bANK ------ \n"
              "1 - Adicionar Conta \n"
              "2 - Alterar Nome \n"
              "3 - Consultar Conta \n"
              "4 - Remover Conta \n"
              "5 - Listar Contas \n"
              "6 - Realizar Saque \n"
              "7 - Realizar Depósito \n"
              "8 - Consultar Saldo \n"
              "9 - Realizar Transferencia \n"
              "10 - Sair")
        opcao = int(input('Selecione uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('Digite o saldo do cliente: '))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o número da conta: '))
            nome = input('Digite o novo nome: ')
            atualizarNome(conta, nome)
        elif opcao == 3:
            conta = int(input('Digite o número da conta: '))
            print(obterConta(conta))
        elif opcao == 4:
            conta = int(input('Digite o número da conta: '))
            deletarConta(conta)
        elif opcao == 5:
            listarContas()
        elif opcao == 6:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite a valor que desejar sacar: '))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite a valor que desejar depositar: '))
            depositar(conta, valor)
        elif opcao == 8:
            conta = int(input('Digite o número da conta: '))
            consultaSaldo(conta)
        elif opcao == 9:
            contaOrigem = int(input('Informe a conta de origim: '))
            contaDestino = int(input('Informe a conta de destino: '))
            valor = float(input('Informe o valor: '))
            transferir(contaOrigem, contaDestino, valor)
        elif opcao == 10:
            print('Até Mais!')
            break
        else:
            print('Opção Invalida!')

menu()