from .clean_cpf import clean_cpf
from .filter_user import filter_user


def create_account(user_cpf: str, list_users: list, list_accounts: list, agency: str = '0001') -> list:
    """
    Cria uma nova conta bancária e a adiciona à lista de contas.

    Valida se o usuário existe na lista de usuários e cria uma nova conta com número sequencial.

    :param user_cpf: CPF do usuário para associar à conta.
    :param list_users: Lista contendo os usuários já cadastrados.
    :param list_accounts: Lista contendo as contas já cadastradas.
    :return: Lista atualizada com a nova conta, ou uma mensagem de erro se o usuário não for encontrado.
    """
    try:
        user_cpf = clean_cpf(user_cpf)

        result, user = filter_user(user_cpf, list_users)
        if not result:
            return 'Usuário não encontrado!'

        # Define o número da agência e o número da conta sequencial
        agency_number = agency
        account_number = len(list_accounts) + 1

        # Cria a nova conta
        new_account = {
            'agency': agency_number,
            'account_number': account_number,
            'user': user
        }

        # Adiciona a nova conta à lista de contas
        list_accounts.append(new_account)

        return list_accounts
    except Exception as error:
        return f'Erro ao criar conta: {error}'


# Teste da função
if __name__ == '__main__':
    users = [
        {
            'name': 'JOÃO',
            'cpf': '12345678900',
            'birth_date': '01/01/2000',
            'address': 'RUA A, 123 - CENTRO - SÃO PAULO/SP'
        }
    ]

    accounts = []

    # Exemplo de criação de conta para um usuário existente
    accounts = create_account('12345678900', users, accounts)
    print(accounts)

    # Exemplo de tentativa de criação de conta para um usuário não existente
    result = create_account('98765432100', users, accounts)
    print(result)
