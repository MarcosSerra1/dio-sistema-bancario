from utils.deposit import deposit_function as deposit
from utils.extract import extract_function as extract
from utils.withdrawal import withdrawal_function as withdrawal
from utils.header import print_header
from utils.create_user import create_user
from utils.create_account import create_account
from utils.list_accounts import list_accounts
from utils.list_users import list_users


if __name__ == '__main__':
    LIMIT_DAY_WITHDRAWAL = 3
    AGENCY = '0001'

    account_balance = 0
    daily_withdrawal = 0
    limit_withdrawal = 500
    transactions = []
    users = []
    accounts = []

    while True:
        option = print_header(version='2.0.0')

        try:
            if option == '1':
                extract_message = extract(
                    account_balance,
                    transactions=transactions
                )

                print(extract_message)

            elif option == '2':
                deposit_amount = input('Digite o valor do depósito: ')

                account_balance, message = deposit(
                    deposit_amount,
                    account_balance,
                    transactions
                )

                print(message)

            elif option == '3':
                withdrawal_value = input('Digite o valor do saque: ')

                account_balance, message = withdrawal(
                    withdrawal_value=withdrawal_value,
                    account_balance=account_balance,
                    transactions=transactions,
                    limit_withdrawal=limit_withdrawal,
                    limit_day_withdrawal=LIMIT_DAY_WITHDRAWAL,
                    number_withdrawal=daily_withdrawal
                )
                print(message)
                daily_withdrawal += 1
            
            elif option == '4':
                user_name = input('Digite o nome do usuário: ')
                user_cpf = input('Digite o CPF do usuário: ')
                user_birth_date = input('Digite a data de nascimento do usuário: ')
                user_address = input('Digite o endereço do usuário (Logradouro, Número - Bairro - Cidade/UF): ')
                result = create_user(
                    user_name=user_name,
                    user_cpf=user_cpf,
                    user_birth_date=user_birth_date,
                    user_address=user_address,
                    list_users=users
                )

                if isinstance(result, list):
                    users = result
                    print('Usuário criado com sucesso!')
                else:
                    print(result)

            elif option == '5':
                list_users(users)

            elif option == '6':
                user_cpf = input('Digite o CPF do usuário para criar a conta: ')
                result = create_account(
                    user_cpf=user_cpf,
                    list_users=users,
                    list_accounts=accounts,
                    agency=AGENCY
                )

                if isinstance(result, list):
                    accounts = result
                    print('Conta criada com sucesso!')
                else:
                    print(result)

            elif option == '7':
                list_accounts(accounts)

            elif option == '0':
                break

            else:
                print('Opção inválida')

        except Exception as error:
            print(f'Erro ao realizar operação: {error}')

        print('\n\n')
        input('Pressione <ENTER> para continuar...')
        print('\n\n')
