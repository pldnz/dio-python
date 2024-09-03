menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    ## Depositar
    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))

        if valor <= 0:
            print("Valor inválido")
            continue
        elif valor > 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("Valor inválido")

    ## Sacar
    elif opcao == "s":
        valor = float(input("Digite o valor a sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente")
        elif excedeu_limite:
            print("Limite excedido")
        elif excedeu_saques:
            print("Limite de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor inválido")

    ## Extrato
    elif opcao == "e":
        print(f"=== Extrato ===")
        print(f"Movimentações do dia: {numero_saques}")
        print(f"Saldo: R$ {saldo:.2f}")
        print("================")

    ## Sair
    elif opcao == "q":
        break

    ## Opção inválida
    else:
        print("Opção inválida")


  
        
    