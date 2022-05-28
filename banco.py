from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta

contas: List[Conta] = []

def main():
    menu()

def menu():
    print("=========================")
    print("====== Victor Bank ======")
    print("=========================")

    print("Selecione uma opção:")
    print("1. Criar conta")
    print("2. Efetuar saque")
    print("3. Efetuar depósito")
    print("4. Efetuar transferência")
    print("5. Listar contas")
    print("6: Sair do sistema")

    opcao = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Até mais!")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida.")
        sleep(2)
        menu()


def criar_conta():
    print("Informe os dados do cliente: ")

    nome = input("Informe o nome do cliente: ")
    email = input("Infrome o email do cliente: ")
    cpf = input("Informe o cpf do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente: ")

    cliente = Cliente(nome, email, cpf, data_nascimento)

    conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso!!")
    print("Dados da conta: ")
    print("==========================")
    print(conta)
    sleep(2)
    menu()


def efetuar_saque():
    if len(contas) > 0:
        numero = int(input("Informe o número da sua conta: "))

        conta = buscar_conta_por_numero(numero)

        if conta:
            valor = float(input("Informe o valor do saque: "))

            conta.sacar(valor)

        else:
            print(f"Não foi encontrada a conta com número {numero}")
        sleep(2)
        menu()
    else:
        print("Ainda não existem contas cadastradas.")
        sleep(2)
        menu()

def efetuar_deposito():
    if len(contas) > 0:
        numero = int(input("Informe o número da conta: "))

        conta = buscar_conta_por_numero(numero)

        if conta:
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)
            sleep(2)
            menu()
        else:
            print(f"Não foi encontrada a conta com número {numero}")
            sleep(2)
            menu()
    else:
        print("Ainda não existem contas cadastradas.")
        sleep(2)
        menu()

def efetuar_transferencia():
    if len(contas) > 0:
        numero_origem = int(input("Informe o número da conta de origem: "))

        conta_origem = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino = int(input("Informe o número da conta de destino: "))

            conta_destino = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor = float(input("informe o valor que vai ser transferido: "))

                conta_origem.transferir(conta_destino, valor)
        else:
            print(f"A sua conta {conta_origem} não foi encontrada.")
        sleep(2)
        menu()
    else:
        print("Ainda não existem contas cadastradas.")
        sleep(2)
        menu()

def listar_contas():
    if len(contas) > 0:
        print("Listagem de Contas: ")

        for conta in contas:
            print(conta)
            print("\n")
            sleep(1)
        sleep(2)
        menu()
    else:
        print("Ainda não esistem contas cadastradas!")
        sleep(2)
        menu()

def buscar_conta_por_numero(numero) -> Conta:
    c = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    
    return c

if __name__ == '__main__':
    main()

