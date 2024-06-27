<h1>
    <span>DESAFIO DIO - Bootcamp Python AI Backend Developer</span>
</h1>

## Objetivo
Repositório criado para concluir o desafio proposto pela  [DIO](https://www.dio.me/): **Modelando um Sistema Bancário com POO**

## Versões anteriores:

[![Versão 1.0](https://img.shields.io/badge/Versão%201.0-E94D5F?style=for-the-badge)](https://github.com/camila-vieirao/sistema-bancario-v1) 
[![Versão 2.0](https://img.shields.io/badge/Versão%202.0-30A3DC?style=for-the-badge)](https://github.com/camila-vieirao/sistema-bancario-v2) 


## O que há de novo?   

O novo sistema possui **classes** para cliente e operações bancárias. Dessa forma, **os dados dos clientes e das contas bancárias são armazenados em objetos ao invés de dicionários**.

## Diagrama de classes:
```mermaid
classDiagram

    Transacao <|-- Deposito
    Transacao <|-- Saque
    Historico "-transacoes" o-- "*" Transacao
    Conta *-- "-historico 1" Historico
    Conta <|-- ContaCorrente
    Conta "* -contas" *-- "1 -cliente" Cliente
    Cliente <|-- PessoaFisica
    Transacao "*" -- Cliente

    <<Interface>> Transacao

    class Transacao {
        +registrar(conta: Conta)
    }

    class Historico {
        +adicionar_trasacao(transacao: Transacao)
    }

    class Conta {
        -saldo : float
        -numero : int
        -agencia : str
        -cliente : Cliente
        - historico : Historico
        +saldo() float
        +nova_conta(cliente : Cliente, numero : int) Conta
        +sacar(valor : float) bool
        +depositar(valor : float) bool 

    }

    class ContaCorrente {
        -limite : float
        -limite_saques : int
    }

    class Cliente {
        -endereco : str
        -contas : list
        +realizar_transacao(conta : Conta, transacao : Transacao)
        +adicionar_conta(conta : Conta)
    }

    class PessoaFisica {
        -cpf : str
        -nome : str
        -data_nascimento : date
    }

    class Deposito {
        -valor : float
    }

    class Saque {
        -valor : float
    }
```

## Requisitos para o Desafio:

### 1. Função Saque   
- A função saque recebe os argumentos **apenas por nome** (*keyword only*).

### 2. Função Depósito
- A função depósito recebe argumentos **apenas por posição** (*positional only*).

### 3. Função Extrato
- A função extrato recebe os argumentos por **posição e por nome**.

### 4. Criar Usuário
- O programa armazena os usuários em uma lista.
- Um **Usuário** deve ser composto por: **nome, data de nascimento, CPF e endereço**.
- O **Endereço** é uma string com o formato: **logradouro, num - bairro - cidade/UF**.
> ⚠️ **Não é possível cadastrar dois usuários com o mesmo CPF.**

### 5. Criar Conta Corrente
- O programa armazena as contas em uma lista.
- Uma **Conta** é composta por: **agência, número da conta, e usuário**.
- O número da conta é sequêncial, iniciando em 1. O número da agência é fixo: "0001".
> ⚠️ **Um usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.**