membro = input("Qual seu nome? ")
startup = input("Nome da startup? ")
ano = input("Qual ano de fundação? ")
v_conta = float(input("Qual valor da conta? "))
q_membros = int(input("Quantos vão dividir a conta? "))

calculo = v_conta / q_membros 

print("===============================================")
print(f"O nome do funcionario:"f"{membro:}")
print(f"O nome da Startup:"f"{startup:}")
print(f"O ano de fundação:"f"{ano:}")
print(f"Valor da conta:"f"{v_conta:}")
print(f"Quantidade que vai dividir a conta:"f"{q_membros:}")
print(f"Resultado da conta:"f"{calculo:}")
print("===============================================")

 