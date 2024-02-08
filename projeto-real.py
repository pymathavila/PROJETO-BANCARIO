nome_cliente = "Matheus Avila"
saldo = 500.0
limite_saque = 500.0
deposito = 0.0
total_depositado = 0.0
saldo_formatado = "R$ {:.2f}".format(saldo) 
limite_formatado_de_saque = "R${:.2f}".format(limite_saque)
saque = 0.0
total_saque = 0.0
tentativas = 0
max_tentativas = 3

print("SEJA BEM-VINDO AO NOSSO BANCO.")
print("Como podemos ajuda-lo hoje, Sr", nome_cliente,"?")

while True:
    opcoes = int(input("Escolha uma opção - [1]Depósito [2]Saque [3]Extrato [4]Sair\n"))

    if opcoes == 1:
        print("Depósito")

        while True:
            print("Seu saldo atualmente é de",saldo_formatado)
            deposito = float(input("Informe o valor que deseja depositar: \n")) 
            if deposito <= 0:
                print("O depósito não foi feito corretamente.")
                continue
            saldo += deposito
            total_depositado += deposito
            saldo_formatado = "R$ {:.2f}".format(saldo) 
            print("Seu saldo após o depósito é de: ",saldo_formatado)
            operacao = int(input("[1]VOLTAR [2]CONTINUAR A OPERAÇÃO [3]SAIR \n"))
            if operacao == 1:
                break
            elif operacao == 2:
                continue
            elif operacao == 3:
                print("Estamos felizes em ajuda-lo")
                quit()
            else:
                print("Operação Inválida.")
    elif opcoes == 2:
        print("Saque")

        while tentativas < max_tentativas:
            saque = float(input("Insira o valor que deseja sacar: \n"))
            if saque <= saldo:
                saldo -= saque
                total_saque += saque
                saldo_formatado = "R${:.2f}".format(saldo)
                tentativas += 1
                print("Seu saldo agora é de: ",saldo_formatado)
                operacao = int(input("[1]VOLTAR [2]CONTINUAR A OPERAÇÃO [3]SAIR \n"))
                if operacao == 1:
                    break
                elif operacao == 2:
                    continue
                elif operacao == 3:
                    print("Estamos felizes em ajuda-lo")
                    quit()
                else:
                    print("Operação inválida.")
                    break
            elif saque > limite_saque:
                print("Impossível realizar o saque. Limite de",limite_formatado_de_saque)
            else:
                print("Você não tem mais saldo.")
                break
        else:
            print("Seus saques foram esgotados, retorne ao menu e selecione uma nova opção.")
    elif opcoes == 3:
        while True:
            opcao = int(input("Selecione um menu para verificar \n [1] Total depositado [2] Total sacado [3] Saldo [4] Menu\n"))
            if opcao == 1:
                print("O total depositado foi: R$",total_depositado)
            elif opcao == 2:
                print("O total sacado foi: R$",total_saque)
            elif opcao == 3:
                print("Seu saldo é de",saldo_formatado)
            elif opcao == 4:
                break
            else:
                print("Operação Inválida")
                quit()
    elif opcoes == 4:
        print("Agradecemos por usar nossos serviços, até mais.")
        quit()