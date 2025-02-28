import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def withdrawal_function(withdrawal_value, account_balance = 0, limit_withdrawal = 500, transactions=[]):
    '''
    Função para realizar saque na conta do usuário
    :param withdrawal_value: Valor do saque
    :param account_balance: Saldo da conta do usuário
    :return: Novo saldo da conta e mensagem de sucesso ou erro
    '''
    try:
        withdrawal_value = float(withdrawal_value)
        account_balance = float(account_balance)

        if withdrawal_value <= account_balance:
            if  withdrawal_value > 0 and withdrawal_value <= limit_withdrawal:
                account_balance -= withdrawal_value
                transactions.append(f'Saque de {locale.currency(withdrawal_value, grouping=True)}')
                message = f'Saque de {locale.currency(withdrawal_value, grouping=True)} realizado com sucesso! Seu novo saldo é de {locale.currency(account_balance, grouping=True)}'
                return account_balance, message
            else:
                return account_balance, 'Valor do saque deve ser maior que zero e menor ou igual a R$ 500,00'

        else:
            return account_balance, f'Saldo insuficiente para realizar o saque de {locale.currency(withdrawal_value, grouping=True)}. Saldo atual: {locale.currency(account_balance, grouping=True)}'

    except ValueError:
        return account_balance, 'Valor do saque deve ser um número!'
    except Exception as error:
        return account_balance, f'Erro ao realizar saque: {error}'


# Teste da função
if __name__ == '__main__':
    saque = withdrawal_function(500, 500)
    print(saque)

# só posso realalizar 3 saques diarios de até R$ 500,00