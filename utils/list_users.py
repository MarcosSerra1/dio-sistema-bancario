def list_users(users):
    """
    Função para listar usuários.

    Args:
    users (list): Lista de dicionários contendo informações dos usuários.

    Returns:
    None
    """
    if not users:
        print("Nenhum usuário encontrado.")
        return

    print(f"{'='*50}")
    print(f"| {'Lista de usuários':^46} |")
    print(f"{'='*50}")

    for user in users:
        print('-' * 50)
        print(f"| {'Nome: ' + user['name']:^46} |")
        print(f"| {'CPF: ' + user['cpf']:^46} |")
        print(f"| {'Data de Nascimento: ' + user['birth_date']:^46} |")
        print(f"| {'Endereço: ' + user['address']:^46} |")
        print('-' * 50)

# Teste da função
if __name__ == '__main__':
    users = [
        {
            'name': 'JOÃO',
            'cpf': '12345678900',
            'birth_date': '01/01/2000',
            'address': 'RUA A, 123 - CENTRO - SÃO PAULO/SP'
        },
        
    ]

    list_users(users)
