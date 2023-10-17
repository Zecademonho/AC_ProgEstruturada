"""
AC5_ProgEstruturada
Estudo dirigido
"""

#piramide
def imprimir (n):
    for i in range (1, n+1):
        for j in range (1, i+1):
            print(j, end="   ")
        print()

n = int(input("insira N:"))
imprimir(n)


#contar digitos
def contar_digitos(numero):
    if numero == 0:
        return 1  # 0 tem um dígito
    contagem = 0
    while numero > 0:
        contagem += 1
        numero = numero // 10
    return contagem

num = int(input("Insira o numero: "))
print(f"Quantidade de digitos é igual a {contar_digitos(num)}")


#divisao
def divisao():
    while True:
        resultado = None
        try: 
            num1 = int(input("Insira de coeficiente: "))
            num2 = int(input("Insira seu divisor: "))
            resultado = num1/num2
        except (ValueError, ZeroDivisionError):
            print("Erro! Não é possível dividir por zero ou insira um valor valido. Tente novamente!")
        else:
            break
        finally:
            if resultado != None:
                print(resultado)

divisao()
