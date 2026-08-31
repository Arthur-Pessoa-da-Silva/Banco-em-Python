from datetime import datetime


def depositar(saldo, historico):
    print("=" * 30)
    print("Você escolheu depositar")
    print("=" * 30)

    try:
        deposito = float(input("Quanto deseja depositar? "))
    except ValueError:
        print("Digite um valor válido!")
        return saldo

    if deposito > 0:
        saldo += deposito

        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

        historico.append(
            f"Depósito: R$ {deposito:.2f} | {data_hora}"
        )

        print("Depósito realizado!")
    else:
        print("Valor inválido")

    return saldo


def sacar(saldo, historico, quantidade_saques, limite_saques):

    print("=" * 30)
    print("Você escolheu sacar")
    print("=" * 30)

    limite_valor_saque = 500

    try:
        valor_saque = float(input("Deseja sacar quanto? "))
    except ValueError:
        print("Digite um valor válido!")
        return saldo, quantidade_saques

    if valor_saque <= 0:
        print("Valor inválido")

    elif valor_saque > saldo:
        print("Saldo insuficiente")

    elif valor_saque > limite_valor_saque:
        print("Você passou do limite de R$ 500 por saque")

    elif quantidade_saques >= limite_saques:
        print("Limite de saques atingido")

    else:
        saldo -= valor_saque
        quantidade_saques += 1

        saques_restantes = limite_saques - quantidade_saques

        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

        historico.append(
            f"Saque: R$ {valor_saque:.2f} | {data_hora}"
        )

        print("Saque realizado!")
        print(f"Saques restantes: {saques_restantes}")

    return saldo, quantidade_saques


def mostrar_saldo(saldo):
    print("=" * 30)
    print(f"Seu saldo é: R$ {saldo:.2f}")
    print("=" * 30)


def mostrar_historico(historico):
    print("=" * 30)
    print("Seu histórico")
    print("=" * 30)

    if len(historico) == 0:
        print("Nenhuma transação realizada.")
    else:
        for numero, transacao in enumerate(historico, start=1):
            print(f"{numero}. {transacao}")