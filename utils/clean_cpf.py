import re

def clean_cpf(cpf: str) -> str:
    """
    Remove quaisquer caracteres que não sejam dígitos do CPF.

    :param cpf: String com o CPF (pode conter pontos, hífen, etc).
    :return: CPF composto apenas pelos dígitos.
    
    Exemplo:
        clean_cpf("123.456.789-00") -> "12345678900"
    """
    cleaned_cpf = re.sub(r'\D', '', cpf)

    if not cleaned_cpf.isdigit():
        raise ValueError('CPF deve conter apenas números!')
    
    return cleaned_cpf
