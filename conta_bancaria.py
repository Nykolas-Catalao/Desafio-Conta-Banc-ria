menu = """
=============== MENU ===============
              
Seja bem vindo! Escolha uma das 
opções abaixo:
              
[d] - Depositar
[s] - Sacar
[e] - Exibir extrato
[q] - Sair
        
====================================      
"""

LIMITE_SAQUE = 500
LIMITE_NUMERO_SAQUES = 3
saldo = 0
numero_saque = 0
historico_de_transação = []

def deposito(valor):
    global saldo
    global historico_de_transação
    if valor > 0:
        saldo += valor 
        historico_de_transação.append(f"+++ Depósito no valor de R${valor:.2f} .")
    else:
        print("\n\nValor digitado inválido. Informe uma quantia válida!")
        

def sacar(valor):
    global saldo
    global numero_saque
    global historico_de_transação
    if (valor > 0) and (valor <= saldo) and (numero_saque < LIMITE_NUMERO_SAQUES) and (valor <= 500):
        saldo -= valor
        numero_saque += 1
        historico_de_transação.append(f"--- Saque no valor de R${valor:.2f} .")
    elif numero_saque >= LIMITE_NUMERO_SAQUES:
        print("\n\nNúmero de saques atingiu o limite! Não foi possível sacar.")
    elif valor <= 0:
        print("\n\nValor de retirada inválido! Informe uma quantia válida.")
    elif valor > 500:
        print(f"\n\nNão foi possível sacar pois o valor de saque ultrapassou o limite!\nValor limite para sacar é R${LIMITE_SAQUE:.2f} .")
    elif valor > saldo:
        print("\n\nNão foi possível realizar o saque! Não há saldo o suficiente.")

def extrato():
    global saldo
    global historico_de_transação
    if historico_de_transação:
        total = f"Saldo Total: R${saldo:.2f} ."
        titulo = "EXTRATO"
        print("#" * 36)
        print(titulo.center(36))
        for i in range(len(historico_de_transação)):
            transacao = historico_de_transação[i]
            print(transacao.center(36))
        print("-" * 36)
        print(total.center(36))
        print("#" * 36)
    else:
        texto = "\nNão foram realizadas movimentações.\n"
        print("#" * 36)
        print(texto.center(36))
        print("#" * 36)
    



while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("Informe o valor que você deseja depositar: "))
            deposito(valor)
        case "s":
            valor = float(input("Informe o valor a ser retirado da conta: "))
            sacar(valor)
        case "e":
            print("\nExibindo extrato...")
            extrato()
        case "q":
            print("\nSaindo do programa...")
            break
        case _:
            print("\nComando inválido! Selecione uma opção válida.\n")
    print("\n\n")