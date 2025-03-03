import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def withdrawal_function(withdrawal_value, account_balance=0, limit_withdrawal=500, number_withdrawal=0, limit_day_withdrawal=3, transactions=[]):
    """
    Função para realizar saque na conta do usuário.

    Esta função recebe um valor de saque, o saldo atual da conta, o limite de saque e a lista de transações,
    valida o valor do saque, atualiza o saldo da conta e registra a transação na lista de transações.

    :param withdrawal_value: Valor do saque (pode ser uma string ou um número).
    :param account_balance: Saldo atual da conta do usuário (padrão é 0).
    :param limit_withdrawal: Limite máximo permitido para o saque (padrão é 500).
    :param number_withdrawal: Número de saques realizados na conta (padrão é 0).
    :param limit_day_withdrawal: Limite diário de saques permitidos (padrão é 3).
    :param transactions: Lista de transações realizadas na conta.
    :return: Novo saldo da conta e mensagem de sucesso ou erro.
    """
    try:
        if number_withdrawal >= limit_day_withdrawal:
            return account_balance, f'Limite diário de saques atingido!'
        else:
            withdrawal_value = float(withdrawal_value)
            account_balance = float(account_balance)

            if withdrawal_value <= account_balance:
                if withdrawal_value > 0 and withdrawal_value <= limit_withdrawal:
                    account_balance -= withdrawal_value
                    transactions.append(f'Saque de {locale.currency(withdrawal_value, grouping=True)}')
                    message = f'Saque de {locale.currency(withdrawal_value, grouping=True)} realizado com sucesso! Seu novo saldo é de {locale.currency(account_balance, grouping=True)}'
                    return account_balance, message
                else:
                    return account_balance, f'Valor do saque deve ser maior que zero e menor ou igual a {locale.currency(limit_withdrawal, grouping=True)}'
            else:
                return account_balance, f'Saldo insuficiente para realizar o saque de {locale.currency(withdrawal_value, grouping=True)}. Saldo atual: {locale.currency(account_balance, grouping=True)}'
    except ValueError:
        return account_balance, 'Valor do saque deve ser um número!'
    except Exception as error:
        return account_balance, f'Erro ao realizar saque: {error}'
