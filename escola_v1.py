#!/user/bin/env python3

"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que 
frequêntam cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo","Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Listar alunos em cada atividade por sala
aula_ingles_sala1 = []
aula_ingles_sala2 = []

atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

for nome_atividade, atividades in atividades:

    print("=-" * 15)
    print(f"Atividade de {nome_atividade}")
    print("=-" * 15)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividades:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    print("Sala 1:", atividade_sala1)
    print("Sala 2:", atividade_sala2)
    print()