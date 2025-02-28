import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF8')

def extract_function(account_balance, transactions):
    '''
    Função para realizar extrato da conta do usuário
    :param account_balance: Saldo da conta do usuário
    :param transactions: Lista de transações realizadas
    :return: Mensagem com o saldo da conta e histórico de transações
    '''
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
