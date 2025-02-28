import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def deposit_function(deposit_amount, account_balance=0, transactions=[]):
    '''
    Função para realizar depósito na conta do usuário
    :param deposit_amount: Valor do depósito
    :param account_balance: Saldo da conta do usuário
    :return: Novo saldo da conta e mensagem de sucesso ou erro
    '''
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


# Teste da função
if __name__ == '__main__':
    deposito = deposit_function(30000)
    print(deposito)
    deposito = deposit_function('500')
    print(deposito)
