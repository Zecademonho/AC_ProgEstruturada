"""
1- num primo
"""

def e_primo(num):
    primo = True
    for div in range (2, num-1):
       if num % div == 0:
        print(div)
        primo = False
    
    if primo == True:
        print("é primo")
    else:
       print("Nao é primo")


e_primo(5)




"""
2- divida
"""
divida= float(input("divida: "))

def det_tx_juros(n):
    if n == 1:
        parc_juros = 1
    if n == 3:
        parc_juros = 0.1
    if n == 6:
        parc_juros = 0.15
    if n == 9:
        parc_juros = 0.2
    if n == 12:
        parc_juros = 0.25
    return parc_juros

def s_data(divida, n):
    juros= divida * det_tx_juros(n)
    valor_juros= divida * juros
    valor_total= valor_juros + divida
    valor_parc= valor_total / n
    print(valor_juros, valor_total, n, valor_parc)

def opcoes_divida(divida):
    print("Valor do juros  Valor Total  Quantidade de parcelas  Valor da parcela")
    print("0 R$", divida, "1 R$", divida)
    for n in range (3, 13, 3):
        s_data(divida, n)

opcoes_divida(divida)



"""
3- numeros
"""
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

# Loop infinito para ler números até que um número negativo seja inserido
while True:
    num = int(input("Digite seu numero: "))
    
    if num < 0:
        break  
    
    if num >= 0 and num <= 25:
        intervalo1 += 1
    elif num <= 50:
        intervalo2 += 1
    elif num <= 75:
        intervalo3 += 1
    elif num <= 100:
        intervalo4 += 1

# Exibe o resultado
print(f"Números no intervalo [0-25]: {intervalo1}")
print(f"Números no intervalo [26-50]: {intervalo2}")
print(f"Números no intervalo [51-75]: {intervalo3}")
print(f"Números no intervalo [76-100]: {intervalo4}")
