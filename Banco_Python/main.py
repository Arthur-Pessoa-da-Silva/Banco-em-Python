import os

from banco import (
    depositar,
    sacar,
    mostrar_saldo,
    mostrar_historico
)

from usuario import (
    cadastro_usuario,
    verificar_senha
)

from dados import (
    salvar_dados,
    carregar_dados
)


saldo = 0.00
opcao = 0
historico = []

limite_saques = 3
quantidade_saques = 0


# Verifica se já existem dados salvos
if os.path.exists("dados.json"):

    dados = carregar_dados()

    nome = dados["nome"]
    senha = dados["senha"]
    saldo = dados["saldo"]
    historico = dados["historico"]
    quantidade_saques = dados["quantidade_saques"]

else:

    print("=" * 30)
    print("       FAÇA SEU CADASTRO")
    print("=" * 30)

    nome, senha = cadastro_usuario()

    salvar_dados(
        nome,
        senha,
        saldo,
        historico,
        quantidade_saques
    )


# Login
if verificar_senha(senha):

    while opcao != 5:

        print("=" * 30)
        print("      Banco em Python")
        print("=" * 30)

        print("""
[1] Depositar
[2] Sacar
[3] Ver saldo
[4] Histórico
[5] Sair
""")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue


        if opcao == 1:

            saldo = depositar(saldo, historico)

            salvar_dados(
                nome,
                senha,
                saldo,
                historico,
                quantidade_saques
            )


        elif opcao == 2:

            saldo, quantidade_saques = sacar(
                saldo,
                historico,
                quantidade_saques,
                limite_saques
            )

            salvar_dados(
                nome,
                senha,
                saldo,
                historico,
                quantidade_saques
            )


        elif opcao == 3:

            mostrar_saldo(saldo)


        elif opcao == 4:

            mostrar_historico(historico)


        elif opcao == 5:

            print("=" * 30)
            print("Obrigado por usar o Banco Python!")
            print("=" * 30)


        else:

            print("Escolha inválida")