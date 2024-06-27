from operacoes import Deposito, Saque

MSG_OPERACOES = '''
    ######## MENU ########
        1. Depósito
        2. Saque
        3. Extrato
        4. Sair
    '''   

def menu_operacoes_bancarias(usuario):
    if not usuario.contas:
        print("Você não possui conta corrente. Crie uma conta primeiro.")
        return

    while True:
        print(MSG_OPERACOES)
        opcao = input("Opção => ")

        if opcao == "1": 
            depositar(usuario)
        elif opcao == "2":
            sacar(usuario)
        elif opcao == "3":
            mostrar_extrato(usuario)
        elif opcao == "4":
            print("\nTchau... :)")
            break
        else: 
            print("Operação inválida.")

def selecionar_conta(usuario):
    print("\nSelecione uma conta:")
    for i, conta in enumerate(usuario.contas, start=1):
        print(f"{i}. Conta {conta.numero} - Saldo: R${conta.saldo:.2f}")

    while True:
        opcao = input("Opção => ")
        try:
            opcao = int(opcao)
            if 1 <= opcao <= len(usuario.contas):
                return usuario.contas[opcao - 1]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Digite um número correspondente à conta.")

def depositar(usuario):
    conta = selecionar_conta(usuario)
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    usuario.realizar_transacao(conta, transacao)

def sacar(usuario):
    conta = selecionar_conta(usuario)
    valor = float(input("Informe o valor do saque: "))
    usuario.realizar_transacao(conta, Saque(valor))

def mostrar_extrato(usuario):
    conta = selecionar_conta(usuario)
    print("\n================ EXTRATO ================")
    for transacao in conta.historico.transacoes:
        print(f"{transacao['data']} - {transacao['tipo']}: R${transacao['valor']:.2f}")
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("==========================================")
