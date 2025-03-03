import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def deposit_function(deposit_amount: float, account_balance: int = 0, transactions: list = []):
    """
    Função para realizar depósito na conta do usuário.

    Esta função recebe um valor de depósito e o saldo atual da conta, valida o valor do depósito,
    atualiza o saldo da conta e registra a transação na lista de transações.

    :param deposit_amount: Valor do depósito (pode ser uma string ou um número).
    :param account_balance: Saldo atual da conta do usuário (padrão é 0).
    :param transactions: Lista de transações realizadas na conta.
    :return: Novo saldo da conta e mensagem de sucesso ou erro.
    """
    try:
        deposit_amount = float(deposit_amount)
        account_balance = float(account_balance)

        if deposit_amount > 0:
            account_balance += deposit_amount
            transactions.append(f'Depósito de {locale.currency(deposit_amount, grouping=True)}')
            message = f'Depósito de {locale.currency(deposit_amount, grouping=True)} realizado com sucesso! Seu novo saldo é de {locale.currency(account_balance, grouping=True)}'
            return account_balance, message
        else:
            return account_balance, 'Valor do depósito deve ser maior que zero!'
    except ValueError:
        return account_balance, 'Valor do depósito deve ser um número!'
    except Exception as error:
        return account_balance, f'Erro ao realizar depósito: {error}'
