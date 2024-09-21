import textwrap

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair

    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor inválido")
    elif valor > 0: 
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso")
    else: 
        print("Valor inválido")

    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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
        print("Saque realizado com sucesso")
    else:
        print("Valor inválido")
    
    return saldo, extrato, numero_saques  # Retorne numero_saques também

def exibir_extrato(saldo, /, *, extrato): 
    print(f"=== Extrato ===")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("================")        

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (apenas números): ")

    if not validar_cpf(cpf):
        print("CPF inválido. Deve conter 11 dígitos numéricos.")
        return

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("CPF já cadastrado")
        return 
    
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço: ")

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado")
        return
    
    # Verificar se o usuário já possui uma conta
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf:
            print("Usuário já possui uma conta.")
            return

    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']} (CPF: {conta['usuario']['cpf']})")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        ## Depositar
        if opcao == "d":
            valor = float(input("Digite o valor a depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        ## Sacar
        elif opcao == "s":
            valor = float(input("Digite o valor a sacar: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        ## Extrato
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        ## Novo usuário
        elif opcao == "nu":
            criar_usuario(usuarios)

        ## Nova conta
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)

            if conta:
                contas.append(conta)
                print("Conta criada com sucesso!")

        ## Listar contas
        elif opcao == "lc":
            listar_contas(contas)

        ## Sair
        elif opcao == "q":
            break

        ## Opção inválida
        else:
            print("Opção inválida")

main()
