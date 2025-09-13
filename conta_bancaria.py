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
historico_de_transação = ""

def deposito(valor):
    global saldo
    global historico_de_transação
    if valor > 0:
        saldo += valor 
        historico_de_transação += f"+++ Depósito no valor de R${valor:.2f} .\n"
    else:
        print("\nValor digitado inválido. Informe uma quantia válida!")
        

def sacar(valor):
    global saldo
    global numero_saque
    global historico_de_transação
    if (valor > 0) and (valor <= saldo) and (numero_saque < LIMITE_NUMERO_SAQUES) and (valor <= 500):
        saldo -= valor
        numero_saque += 1
        historico_de_transação += f"--- Saque no valor de R${valor:.2f} .\n"
    elif valor <= 0:
        print("Valor de retirada inválido! Informe uma quantia válida.")
    elif valor > 500:
        print(f"Não foi possível sacar pois o valor de saque ultrapassou o limite!\nValor limite para sacar é R${LIMITE_SAQUE:.2f} .")
    elif valor > saldo:
        print("Não foi possível realizar o saque! Não há saldo o suficiente.")
    elif numero_saque >= LIMITE_NUMERO_SAQUES:
        print("Número de saques atingiu o limite! Não foi possível sacar.")
    



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
            print("\nextrato")
        case "q":
            print("\nSaindo do programa...")
            break
        case _:
            print("\nComando inválido! Selecione uma opção válida.\n")