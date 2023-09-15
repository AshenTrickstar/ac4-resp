valor = 1000

num_parcelas = 1

def determina_porcentagem_juros(num_parcelas):

    if num_parcelas == 1:
        percentual = 0
    
    if num_parcelas == 3:
        percentual = 0.10
    
    if num_parcelas == 6:
        percentual = 0.15
    
    if num_parcelas == 9:
        percentual = 0.20
    
    if num_parcelas == 12:
        percentual = 0.25 
    return percentual 

def exibir_dados(divida, num_parcelas):
    juros = divida * determina_porcentagem_juros(num_parcelas)
    valor_total = juros + divida
    valor_das_parcelas = valor_total / num_parcelas
    print(juros, valor_total, num_parcelas, valor_das_parcelas)

def opcoes_divida(divida):
    print("Juros / Valor total / Quant. de parcelas / Valor das Parcelas")
    print("0 R$", divida, "1R$", divida)
    for n in range(3, 13, 3):
        exibir_dados(divida, n)
div = float(input("Diga sua dívida: "))

opcoes_divida(div)