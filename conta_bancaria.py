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
saque = 0
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
        

while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("Informe o valor que você deseja depositar: "))
            deposito(valor)
        case "s":
            print("\nsacar")
        case "e":
            print("\nextrato")
        case "q":
            print("\nSaindo do programa...")
            break
        case _:
            print("\nComando inválido! Selecione uma opção válida.\n")