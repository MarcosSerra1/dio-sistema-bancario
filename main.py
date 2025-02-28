import datetime
from utils.deposit import deposit_function as deposit
from utils.extract import extract_function as extract
from utils.withdrawal import withdrawal_function as withdrawal


def print_header():
    now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print('*' * 50)
    print(f"* {'Sistema Bancário com Python - Versão 1.0':^46} *")
    print(f"* {'DIO - Bootcamp Python Developer':^46} *")
    print(f"* {'Data/Hora: ' + now:^46} *")
    print('*' * 50)
    print("Selecione uma opção:")
    print("1 - Extrato")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Sair")

if __name__ == '__main__':
    account_balance = 0
    daily_withdrawal = 0
    LIMIT_DAY_WITHDRAWAL = 3
    limit_withdrawal = 500
    transactions = []

    while True:
        print_header()
        option = input()

        try:
            if option == '1':
                extract_message = extract(account_balance, transactions)
                print(extract_message)

            elif option == '2':
                deposit_amount = input('Digite o valor do depósito: ')
                account_balance, message = deposit(deposit_amount, account_balance, transactions)
                print(message)

            elif option == '3':
                if daily_withdrawal < LIMIT_DAY_WITHDRAWAL:
                    withdrawal_value = input('Digite o valor do saque: ')
                    account_balance, message = withdrawal(withdrawal_value, account_balance, limit_withdrawal, transactions)
                    print(message)
                    daily_withdrawal += 1

                else:
                    print('Limite diário de saques atingido!')

            elif option == '4':
                break

            else:
                print('Opção inválida')

        except Exception as error:
            print(f'Erro ao realizar operação: {error}')

        input('Pressione <ENTER> para continuar...')
        print('\n\n')
