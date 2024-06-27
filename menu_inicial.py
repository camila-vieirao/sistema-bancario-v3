from menu_transacoes import menu_operacoes_bancarias
from operacoes import PessoaFisica, ContaCorrente
from otp import OTPService

MENU = '''
========= BEM-VINDO! =========
Digite uma opção para começar:
    1. Criar Usuário
    2. Criar Conta Corrente
    3. Fazer Login
    4. Sair
==============================
'''

MSG_CRIAR_USUARIO = '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Ótimo! Primeiramente, vamos precisar coletar alguns dados.
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

MSG_CRIAR_CONTA_CORRENTE = '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
     Certo! Vamos criar uma Conta Corrente para você!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

clientes = []
contas = []

def menu_inicio():
    while True:
        print(MENU)
        opcao = input("Opção => ")

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta_corrente()
        elif opcao == "3":
            usuario = login_usuario()
            if usuario:
                if usuario.contas:
                    menu_operacoes_bancarias(usuario)
                else:
                    print("Usuário não possui conta corrente. Crie uma conta primeiro.")
        elif opcao == "4":
            print("Saindo... ")
            break
        else:
            print("Opção inválida. Tente novamente.")

def criar_usuario():
    print(MSG_CRIAR_USUARIO)
    print("\n========= DADOS PESSOAIS =========")
    nome = input("Nome: ").strip()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    cpf_inicio = input("CPF: ").strip()
    cpf = ''.join(filter(str.isdigit, cpf_inicio))

    if any(cliente.cpf == cpf for cliente in clientes):
        print("Usuário com esse CPF já cadastrado.")
        return

    print("\n============ ENDEREÇO ============")
    logradouro = input("Logradouro: ").strip()
    numero_casa = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    uf = input("UF: ").strip().upper()

    endereco = f"{logradouro}, {numero_casa} - {bairro} - {cidade}/{uf}"
    senha = input("Crie uma senha (máximo 4 caracteres): ").strip()
    if len(senha) > 4:
        print("Senha deve ter no máximo 4 caracteres. Cadastro não concluído.")
        return

    optar_otp = input("Deseja ativar autenticação de dois fatores (OTP)? (S/N): ").upper()
    otp_ativo = optar_otp == "S"

    if otp_ativo:
        email = input("Digite seu e-mail para receber o OTP: ")
        otp_digitado = OTPService.enviar_otp_email(email)

        otp_digitado_usuario = input("Digite o OTP recebido por e-mail: ")
        if not OTPService.verificar_otp(otp_digitado_usuario, otp_digitado):
            print("OTP incorreto. Cadastro não concluído.")
            return

    usuario = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco, senha=senha, otp_ativo=otp_ativo)

    clientes.append(usuario)
    print("Cadastro concluído com sucesso!")

def criar_conta_corrente():
    print(MSG_CRIAR_CONTA_CORRENTE)

    cpf_inicio = input("Digite o CPF do usuário: ").strip()
    cpf = ''.join(filter(str.isdigit, cpf_inicio))

    usuario = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
    if usuario is None:
        print("CPF não cadastrado. Crie um usuário primeiro.")
        return

    agencia = "0001"
    numero_conta = len(contas) + 1
    conta = ContaCorrente(numero=numero_conta, cliente=usuario)

    contas.append(conta)
    usuario.adicionar_conta(conta)

    print("Conta criada com sucesso!")
    print(f"Agência: {agencia}")
    print(f"Número da Conta: {numero_conta}")
    print(f"Usuário: {usuario.nome}")

def login_usuario():
    cpf_inicio = input("Digite o CPF do usuário: ").strip()
    cpf = ''.join(filter(str.isdigit, cpf_inicio))

    usuario = next((cliente for cliente in clientes if cliente.cpf == cpf), None)
    if usuario:
        senha = input("Digite a senha: ")
        if usuario.senha == senha:
            if usuario.otp_ativo:
                email = input("Digite seu e-mail para receber a OTP: ")
                otp_digitado = OTPService.enviar_otp_email(email)

                otp_digitado_usuario = input("Digite o OTP recebido por e-mail: ")
                if not OTPService.verificar_otp(otp_digitado_usuario, otp_digitado):
                    print("OTP incorreto. Login não concluído.")
                    return None
            print("Usuário autenticado!")
            return usuario
        else:
            print("Senha incorreta.")
    else:
        print("CPF não cadastrado.")
    return None

