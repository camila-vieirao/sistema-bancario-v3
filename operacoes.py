from abc import ABC, abstractmethod
from datetime import datetime, timezone
LIMITE_DE_TRANSACOES = 10

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if (len(conta.historico.transacoes_do_dia()) >= LIMITE_DE_TRANSACOES):
            print(f"\n Falha na Transação - Número de transações diárias excedido ({LIMITE_DE_TRANSACOES})")
            return
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, senha, otp_ativo=False):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.senha = senha
        self.otp_ativo = otp_ativo

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self._saldo:
            return False
        self._saldo -= valor
        return True

    def depositar(self, valor):
        if valor < 0:
            print("O valor do depósito deve ser positivo.")
            return False
        
        self._saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        saldo_disponivel = self.saldo
        if valor > saldo_disponivel:
            print(f"O valor do saque (R$ {valor:.2f}) excede o saldo disponível (R$ {self.saldo:.2f}).")
            return False
        if valor > self.limite:
            print(f"O valor do saque (R$ {valor:.2f}) excede o limite (R$ {self.limite:.2f}).")
            return False
        numero_saques = len([t for t in self.historico.transacoes if t['tipo'] == 'Saque'])
        if numero_saques >= self.limite_saques:
            print("Limite de saques excedido.")
            return False
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return super().sacar(valor)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now(timezone.utc).strftime("%d-%m-%Y %H:%M:%S"),
        })

    def gerar_relatorio(self, tipo_transacao = None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.now(timezone.utc).date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
