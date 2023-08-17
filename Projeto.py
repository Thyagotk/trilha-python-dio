menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opção = input(menu)

    if opção == "1":
        valor = float(input("Informar o valor que deseja depositar Depositar: "))


        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            


        else:
            print("Operação falhou: o valor digitado é invalido.") 

    elif opção == "2" :
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou: Você não tem saldo suficiente.")

        elif  excedeu_limite:
            print("Operação falhou: Não é possivel retirar essa quantia ")

        elif excedeu_saques:
            print("Operação falhou: Número de saques ja atingido ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print( "Operação falhou: O valor informando é invalido." )

    elif opção == "3":
        print("\n======================  EXTRATO ======================")
        print("Não foram realizadas movimentações." if not extrato else extrato ) 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")

    elif opção == "0":
        break


           

    else:
        print("operação invalida, por favor selecione novamente a opração desejada. ")