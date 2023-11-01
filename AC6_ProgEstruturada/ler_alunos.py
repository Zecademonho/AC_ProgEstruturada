#le o nome, matricula e email e salva num arquivo json assim:
import json

def salvar_dados_aluno(matricula, nome, email):
    # Criando um dicionário com os dados do aluno
    dados = {
        matricula : {
            "nome": nome,
            "email": email,
        }
    }

    # Lendo o arquivo JSON (se ele existir)
    try:
        with open("dados_alunos.json", "r") as file:
            alunos = json.load(file)
    except FileNotFoundError:
        alunos = []

    # Adicionando o novo aluno ao arquivo JSON
    alunos.append(dados)

    # Salvando o arquivo JSON
    with open("dados_alunos.json", "w") as file:
        json.dump(alunos, file, indent=4)

salvar_dados_aluno(matricula = input("matricula: "), nome = input("nome: "), email = input("email: "))

