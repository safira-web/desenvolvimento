banco_projetos = []

def exibir_menu():

    escolha = ""

    while escolha != "3":
        print("1. Cadastrar Projeto")
        print("2. Listar Projetos")
        print("3. Sair")

        escolha = input("Opção (1-3): ")

        if escolha == "1":
            cadastrar_projeto()

        elif escolha == "2":
            listar_projeto()
        elif escolha == "3":
            print("Encerrando o programa...")
        break

def cadastrar_projeto():

    nome_projeto = input("Digite o nome do Projeto: ")
    area_atuacao = input("Digite a area de Atuação: ")
    faturamento = float(input("Digite o faturamento previsto: "))

    projeto = {
        "nome projeto": nome_projeto,
        "área de atuação": area_atuacao,
        "faturamento previsto": faturamento
    }
    banco_projetos.append(projeto)
    print("Projeto cadastrado com sucesso!!!")
    return exibir_menu()



def listar_projeto():
    if len(banco_projetos) == 0:
        print("Nenhum projeto cadastrado!!!")
    else:
        total = 0
        for projeto in banco_projetos:
            print(f"Nome do projeto: {projeto['nome projeto']}")
            print(f"Área de atuação: {projeto['área de atuação']}")
            print(f"Faturamento previsto: {projeto['faturamento previsto']:.2f}")
            total += projeto['faturamento previsto']
    return exibir_menu()



exibir_menu()
