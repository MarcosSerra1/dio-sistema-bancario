from .clean_cpf import clean_cpf
from .filter_user import filter_user


def create_user(user_name: str, user_cpf: str, user_birth_date: str, user_address: str, list_users: list) -> list:
    """
    Cria um novo usuário e o adiciona à lista de usuários, após validar os dados informados.

    Valida o formato do endereço e verifica se o CPF do usuário já está cadastrado.
    O endereço deve seguir o padrão: "Logradouro, Número - Bairro - Cidade/UF".
    
    :param user_name: Nome do usuário.
    :param user_cpf: CPF do usuário (pode conter formatação, como pontos e hífen).
    :param user_birth_date: Data de nascimento do usuário (formato: "DD/MM/AAAA").
    :param user_address: Endereço do usuário no padrão "Logradouro, Número - Bairro - Cidade/UF".
                           Exemplo: "Rua A, 123 - Centro - São Paulo/SP".
    :param list_users: Lista contendo os usuários já cadastrados.
    :return: Lista atualizada com o novo usuário, ou uma mensagem de erro se o CPF já estiver cadastrado.
    """
    try:
        user_cpf = clean_cpf(user_cpf)

        result, user = filter_user(user_cpf, list_users)
        if result:
            return 'Usuário já cadastrado!'

        user_name = user_name.upper()
        user_address = user_address.upper()

        new_user = {
            'name': user_name,
            'cpf': user_cpf,
            'birth_date': user_birth_date,
            'address': user_address
        }

        list_users.append(new_user)

        return list_users

    except ValueError as error:
        return f'Erro ao criar usuário: {error}'
    except Exception as error:
        return f'Erro ao criar usuário: {error}'


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

    # Exemplo de criação de usuário com CPF formatado e endereço válido.
    users = create_user('João', '123.456.789-00', '01/01/2000', 
                        'Rua A, 123 - Centro - São Paulo/SP', users)
    print(users)
