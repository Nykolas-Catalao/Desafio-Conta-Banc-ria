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

while True:
    opcao = input(menu)
    match opcao:
        case "d":
            print("\ndepositar")
        case "s":
            print("\nsacar")
        case "e":
            print("\nextrato")
        case "q":
            print("\nSaindo do programa...")
            break
        case _:
            print("\nComando inválido! Selecione uma opção válida.")