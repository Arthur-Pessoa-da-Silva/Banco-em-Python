def cadastro_usuario():
    nome = input("Digite seu nome: ")
    senha = input("Digite uma senha: ")

    print("Usuário cadastrado com sucesso!")

    return nome, senha


def verificar_senha(senha):
    tentativas = 0
    limite_tentativas = 3

    while tentativas < limite_tentativas:
        senha_digitada = input("Digite sua senha: ")

        if senha_digitada == senha:
            print("Acesso permitido!")
            return True

        tentativas += 1
        print("Senha incorreta!")

    print("Número máximo de tentativas atingido.")
    return False