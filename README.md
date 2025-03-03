# DIO Sistema Bancário com Python

Este é um projeto desenvolvido como parte da trilha de Python da DIO. O projeto simula um sistema de caixa eletrônico utilizando a interface de terminal, permitindo ao usuário realizar operações como extrato, depósito e saque, com validação de limites e registro das transações.

## Funcionalidades

- Exibição de extrato com histórico de transações
- Depósito de valores com formatação monetária
- Saque com limite diário e valor máximo
- Criação de novos usuários
- Criação de novas contas bancárias
- Listagem de usuários cadastrados
- Listagem de contas bancárias
- Interface de terminal com cabeçalho informativo (data/hora, versão do sistema, etc)

## Tecnologias Utilizadas

- Python 3.11
- Módulo `locale` para formatação monetária
- Uso de f-strings para formatação da saída

## Estrutura do Projeto

```
dio-sistema-bancario
├── main.py
└── utils/
    ├── init.py
    ├── clean_cpf.py
    ├── create_account.py
    ├── create_user.py
    ├── deposit.py
    ├── extract.py
    ├── filter_user.py
    ├── header.py
    ├── list_accounts.py
    ├── list_users.py
    └── withdrawal.py
```

## Como Executar

1. Certifique-se de ter o Python 3.11 instalado.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute o arquivo `main.py`:

```bash
   python main.py
```

## Considerações

O sistema está configurado para formatação monetária no padrão brasileiro.
Os limites de operação (como o saque máximo diário) podem ser ajustados de acordo com a necessidade.
O número da agência é fixo como "0001".
O número da conta é sequencial, iniciando em 1.

## Autor

Desenvolvido como desafio da trilha de Python da DIO.

### Explicação das Melhorias

1. **Funcionalidades Adicionadas:**
   - Adicionamos as funcionalidades de criação de novos usuários, criação de novas contas bancárias, listagem de usuários cadastrados e listagem de contas bancárias.

2. **Estrutura do Projeto:**
   - Atualizamos a estrutura do projeto para incluir todos os novos arquivos de utilitários.

3. **Como Executar:**
   - Adicionamos instruções claras sobre como executar o projeto.

4. **Considerações:**
   - Incluímos informações sobre a formatação monetária, limites de operação, número da agência e número da conta.
