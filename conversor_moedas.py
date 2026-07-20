def converter_real_para_dolar(valor_reais, cotacao_dolar):
    
    valor_dolar = valor_reais / cotacao_dolar
    return valor_dolar

valor = float(input("Digite o valor em reais: "))
cotacao = float(input("Digite a cotacao do dólar: "))

resultado = converter_real_para_dolar(valor, cotacao)
print(f"O valor de R${valor:.2f} equivale a {resultado:.2f}")
