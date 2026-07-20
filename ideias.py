opcao = ""
ideia = []

while opcao != "3":
    print("=======MENU========")
    print("1-Adicionar ideia")
    print("2-Listar ideias")
    print("3-Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar = ideia.append(input("Digite sua ideia: "))

    elif opcao == "2":
        if ideia == 0:
            print("Nenhuma ideia cadastrada!")
        else:
            total = len(ideia)
            print(f"Total de ideias: {total}")

            for i in ideia:
                print(f"Ideia :{i}")

    elif opcao == "3":
        print("Encerrando...")

    else:
        print("opção inválida!")    
        
        
        