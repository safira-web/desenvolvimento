import time 

servidores_cadastrados = [
    {"name": "srv-banco", "ip": "192.168.1.10"},
    {"name": "srv-web", "ip": "192.168.1.20"}
]

def exibir_menu_atendimento():
 
    print("1 - Cadastrar novo servidor")
    print("2 - Exibir painel e pingar")
    print("3 - Sair")


while True:


    exibir_menu_atendimento()

    try:
        opcao = int(input("Escolha:"))
    except ValueError:
        print("Erro: digite apenas um número válido.")
        continue

    if opcao == 1:

        nome = input("Hostname: ")
        ip = input("IP:")

        novo = {

            "name": nome,
            "ip": ip
        }

        servidores_cadastrados.append(novo)
        print("Cadastrado")


    elif opcao == 2:
   
        for s in servidores_cadastrados:
            print("Pingando servidor: " + s["name"]) 
            latencias = [10.5, 0, 15.2]
            total_pings = len(latencias)

            if total_pings > 0:
                latencia_media = sum(latencias) / total_pings
                print("Lantência média:",latencia_media)
            else:
                print("Nenhum pacote recebido.")
        try:
            with open("logs/auditoria.log", "a") as arquivo_log:  
               arquivo_log.write("ok\n")
        except FileNotFoundError:
                    print("Erro: a pasta 'logs' não foi encotrada.")   
        except PermissionError:
                print("Erro: sem permissão para gravar o arquivo de log.")  

    elif opcao == 3:
        break
