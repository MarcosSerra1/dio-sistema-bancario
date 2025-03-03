def list_accounts(accounts):
    """
    Função para listar contas bancárias.

    Args:
    accounts (list): Lista de dicionários contendo informações das contas.

    Returns:
    None
    """
    print(f"{'='*50}")
    print(f"| {'Lista de Contas Bancárias':^46} |")
    print(f"{'='*50}")

    if not accounts:
        print(f"| {'Nenhuma conta encontrada.':^46} |")
        print(f"{'='*50}")
        return

    for account in accounts:
        print(f"{'-'*50}")
        print(f"| {'Agência: ' + account['agency']:^46} |")
        print(f"| {'C/C: ' + str(account['account_number']):^46} |")
        print(f"| {'Titular: ' + account['user']['name']:^46} |")
        print(f"{'-'*50}")

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

    accounts = [
        {
            'agency': '0001',
            'account_number': 1,
            'user': users[0]
        }
    ]

    list_accounts(accounts)