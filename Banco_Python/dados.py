import json


def salvar_dados(nome, senha, saldo, historico, quantidade_saques):
    dados = {
        "nome": nome,
        "senha": senha,
        "saldo": saldo,
        "historico": historico,
        "quantidade_saques": quantidade_saques
    }

    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

    print("Dados salvos com sucesso!")


def carregar_dados():
    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)

    return dados