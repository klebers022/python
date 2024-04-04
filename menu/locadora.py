opcao = 0

while opcao !=5:
    print("Sistema de locação")
    print("1 - alugar veiculo")
    print("2 - devolver veiculo")
    print("3 - cadastrar cliente")
    print("4 - consutar veiculo disponivel")
    print("5 - sair")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
            pass
    elif opcao == 2:
            pass
    elif opcao == 3:
        nome = input("digite seu nome:")
        cpf= int(input("CPF: "))
        nascimento = input("nascimento: ")
        habilitacao = int(input("Habilitado: "))
        print("Cadastro realizado com sucesso!")
    elif opcao == 4:
        tipo = input("Informe o tipo do carro: ")
        print("Carros disponiveis:")
        print("Hb20 2023")
        print("gol 2019")
        print("polo 2020")
    elif opcao == 5:
        print("Obrigado por usar nosso sistema")
    else:
        print("opção invalida")    
        

    


