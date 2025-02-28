# DIO Sistema Bancário com Python

Este é um projeto desenvolvido como parte da trilha de Python da DIO. O projeto simula um sistema de caixa eletrônico utilizando a interface de terminal, permitindo ao usuário realizar operações como extrato, depósito e saque, com validação de limites e registro das transações.

## Funcionalidades

- Exibição de extrato com histórico de transações
- Depósito de valores com formatação monetária
- Saque com limite diário e valor máximo
- Interface de terminal com cabeçalho informativo (data/hora, versão do sistema, etc)

## Tecnologias Utilizadas

- Python 3.11
- Módulo `locale` para formatação monetária
- Uso de f-strings para formatação da saída

## Estrutura do Projeto

dio-sistema-bancario
├── main.py
└── utils/
    ├── init.py
    ├── deposit.py
    ├── extract.py
    └── withdrawal.py

## Considerações

- O sistema está configurado para formatação monetária no padrão brasileiro.
- Os limites de operação (como o saque máximo diário) podem ser ajustados de acordo com a necessidade.

## Autor

Desenvolvido como desafio da trilha de Python da DIO.
