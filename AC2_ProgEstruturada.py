"""
Salario Mensal
"""

#Pedindo ao user os valores da horas e o salario/hora
sph= float(input("Insira o salario recebido por hora :"))
h= float(input("Quantidade de horas trabalhadas: "))


#Defininfo funcao salario para calcular o salario a ser recebido
def salario(sph, h):
    return sph * h


#Define funcao main para exibir ao user o salario
def main():
    print("O salario será" , salario(sph, h))


main()



"""
Numeros e Calculo
"""

#Pedindo ao user os valores dos numeros
N1= float(input("Insira seu primeiro numero: "))
N2= float(input("Insira seu segundo numero: "))
N3= float(input("Insira seu terceiro numero: "))


#Definindo funcao numeros para calcular o resultado da conta
def nms(n1, n2, n3 ):
     r1=((n1 * 2) * (n2 / 2))
     r2=((n1 * 3) + (n3))
     r3=(n3 ** 3)
     return r1, r2, r3


#Definindo funcao client numeros para mostrar ao user os resultados
def cli_nms():
    r1, r2, r3= nms(N1, N2, N3)
    print("r1: ", r1)
    print("r2: ", r2)
    print("r3: ", r3)


#Chamando a funcao para iniciar o programa
cli_nms()



"""
Numeros e Calculo, porem somente retornando os resulatdos
"""


#Pedindo ao user os valores dos numeros
N1= float(input("Insira seu primeiro numero: "))
N2= float(input("Insira seu segundo numero: "))
N3= float(input("Insira seu terceiro numero: "))


#Definindo funcao numeros para calcular o resultado da conta
def nms(n1, n2, n3 ):
     r1=((n1 * 2) * (n2 / 2))
     r2=((n1 * 3) + (n3))
     r3=(n3 ** 3)
     return r1, r2, r3


#Definindo funcao client numeros para retornar ao compt os resultados
def cli_nms():
    r1, r2, r3=nms(N1, N2, N3)
    return r1, r2, r3



"""
Ano Bissexto
"""

ano=int(input("Insira seu ano: "))

def bissexto():
    ano_bissexto= (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
    print(ano_bissexto)

bissexto()
##################

