import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF8')

def extract_function(account_balance, transactions):
    """
    Função para gerar o extrato da conta do usuário.

    Esta função recebe o saldo atual da conta e a lista de transações realizadas,
    formata o saldo e o histórico de transações, e retorna uma mensagem com essas informações.

    :param account_balance: Saldo da conta do usuário.
    :param transactions: Lista de transações realizadas na conta.
    :return: Mensagem com o saldo da conta e histórico de transações.
    """
    try:
        account_balance = float(account_balance)
        extract_message = f'Seu saldo é de {locale.currency(account_balance, grouping=True)}\n'
        extract_message += 'Histórico de transações:\n'

        if not transactions:
            return extract_message + 'Nenhuma transação realizada!'
        else:
            for transaction in transactions:
                extract_message += f'{transaction}\n'
        return extract_message
    except ValueError:
        return 'Saldo da conta deve ser um número!'
    except Exception as error:
        return f'Erro ao gerar extrato: {error}'
