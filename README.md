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

## Requisitos - Diagrama de classes:
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

## Autenticação de Dois Fatores: OTP   
Implementei um mecanismo de Autenticação de Dois Fatores (OTP) para oferecer uma camada adicional de segurança aos usuários do sistema bancário.

### Como funciona?

- Durante o cadastro, os usuários têm a opção de ativar a autenticação de dois fatores (OTP).
- Um código OTP é enviado para o e-mail fornecido pelo usuário
    > É possível utilizar um **e-mail temporário** através do [TEMPMAIL](https://temp-mail.org/en/)
- O código OTP é necessário para realizar login e operações sensíveis no sistema, garantindo maior segurança.

## Instruções de Uso

**Para utilizar o sistema bancário:**

1. Clone o repositório para sua máquina local.
2. Execute o programa principal `main.py`  para iniciar o sistema.
3. Siga as instruções fornecidas no terminal para criar contas, realizar transações e visualizar extratos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, novas funcionalidades ou reportar problemas encontrados.

