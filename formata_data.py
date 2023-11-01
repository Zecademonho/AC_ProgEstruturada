from datetime import datetime

def formata_data(data):
    try:
        # Converte a data no formato DD/MM/AAAA para um objeto datetime
        data = datetime.strptime(data, '%d/%m/%Y')

        # Extrai o dia, mês e ano do objeto datetime
        dia = data.day
        mes = data.month
        ano = data.year

        # Mapeia os meses para os respectivos nomes por extenso
        meses_por_extenso = {
            1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
            7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
        }

        # Retorna a data formatada no formato de mesPorExtenso
        return (f'{dia} de {meses_por_extenso[mes]} de {ano}')

    except ValueError:
        # Caso a data seja inválida, retorna None
        return None

print(formata_data(input("Insira a data: ")))