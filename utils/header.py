import datetime

def print_header(version: str):
    """
    Imprime o cabeçalho do sistema bancário com informações detalhadas.

    O cabeçalho inclui o nome do sistema, a versão, o nome do bootcamp, a data e hora atuais,
    e as opções disponíveis para o usuário.

    :param version: Versão do sistema a ser exibida no cabeçalho.
    """
    now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print('*' * 50)
    print(f"* {'Sistema Bancário com Python - Versão ' + version:^46} *")
    print(f"* {'DIO - Bootcamp Python Developer':^46} *")
    print(f"* {'Data/Hora: ' + now:^46} *")
    print('*' * 50)
    print(f"* {'Selecione uma opção:':^46} *")
    print(f"* {'1 - Extrato':<46} *")
    print(f"* {'2 - Depósito':<46} *")
    print(f"* {'3 - Saque':<46} *")
    print(f"* {'4 - Criar Usuário':<46} *")
    print(f"* {'5 - Listar Usuários':<46} *")
    print(f"* {'6 - Criar Conta':<46} *")
    print(f"* {'7 - Listar Contas':<46} *")
    print(f"* {'0 - Sair':<46} *")
    print("\n")

    return input('=> ')
