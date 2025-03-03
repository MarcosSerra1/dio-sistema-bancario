def filter_user(user_cpf: str, list_users: list) -> tuple:
    """
    Verifica se um usuário com o CPF informado já está cadastrado.

    :param user_cpf: CPF do usuário a ser verificado.
    :param list_users: Lista contendo os usuários já cadastrados.
    :return: Tupla contendo um booleano indicando se o usuário foi encontrado e o usuário (ou None se não encontrado).
    """
    for user in list_users:
        if user_cpf == user['cpf']:
            return True, user
    return False, None
