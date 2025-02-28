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
    print("Selecione uma opção:")
    print("1 - Extrato")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Sair")
