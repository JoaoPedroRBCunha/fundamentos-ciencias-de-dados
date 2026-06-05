"""
Aula 7 - Estruturas de Dados em Python
Responsavel: Maximo Henrique Fortinho De Miranda Sa Neto
Papel: Desenvolvedor de Notebooks e Dados
"""


def divisao(titulo):
    print("\n" + "=" * 70)
    print(titulo)
    print("=" * 70)


# SLIDE 2 - FUNDAMENTOS
divisao("SLIDE 2 - O que sao estruturas de dados?")

print("Estruturas de dados organizam informacoes dentro do programa.")
print("Em Ciencia de Dados, elas ajudam a coletar, limpar, transformar e analisar dados.")
print("Exemplos em Python: listas, tuplas, dicionarios e conjuntos.")


# SLIDE 3 - LISTAS
divisao("SLIDE 3 - Listas")

notas = [8.5, 7.0, 9.0]

print("Lista inicial:", notas)
print("Acessando o primeiro item:", notas[0])

notas.append(6.5)
print("Depois do append(6.5):", notas)

notas.remove(7.0)
print("Depois do remove(7.0):", notas)

notas[1] = 10.0
print("Depois de alterar o indice 1:", notas)


# SLIDE 4 - TUPLAS
divisao("SLIDE 4 - Tuplas")

ponto = (10, 20)
periodo = ("2025", "S1")

print("Ponto fixo:", ponto)
print("Ano do periodo:", periodo[0])
print("Semestre do periodo:", periodo[1])


# SLIDE 4 - CONJUNTOS
divisao("SLIDE 4 - Conjuntos")

skills = {"python", "sql", "python"}

print("Conjunto de skills:", skills)
print("Existe python no conjunto?", "python" in skills)

skills.add("excel")
print("Depois de adicionar excel:", skills)


# SLIDE 5 - DICIONARIOS
divisao("SLIDE 5 - Dicionarios")

aluno = {"nome": "Ana", "idade": 20}

print("Dicionario inicial:", aluno)
print("Acessando o nome:", aluno["nome"])

aluno["curso"] = "Dados"
print("Depois de inserir curso:", aluno)

aluno["idade"] = 21
print("Depois de atualizar idade:", aluno)

del aluno["curso"]
print("Depois de remover curso:", aluno)


# SLIDE 6 - DATASET DE ALUNOS
divisao("SLIDE 6 - Dataset de alunos")

turma = [
    {
        "nome": "Ana",
        "idade": 20,
        "curso": "Dados",
        "notas": [8.5, 7.0, 9.0],
        "skills": {"python", "sql"},
    },
    {
        "nome": "Bruno",
        "idade": 22,
        "curso": "Dados",
        "notas": [5.0, 6.5, 4.0],
        "skills": {"excel"},
    },
    {
        "nome": "Carla",
        "idade": 19,
        "curso": "Dados",
        "notas": [9.5, 8.0, 10.0],
        "skills": {"python", "r"},
    },
]

print("Turma completa:")
for aluno in turma:
    print(aluno)


# SLIDE 7 - ANALISE DOS DADOS
divisao("SLIDE 7 - Media, situacao e grafico no terminal")

for aluno in turma:
    notas = aluno["notas"]
    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperacao"
    else:
        situacao = "Reprovado"

    barra = "#" * int(media)
    print(f"{aluno['nome']:<6} {barra:<9} {round(media, 1):<4} {situacao}")


# SLIDE 8 - FUNCAO PARA RESUMIR A TURMA
divisao("SLIDE 8 - Funcao para resumir a turma")


def resumo_turma(turma):
    medias = [
        sum(aluno["notas"]) / len(aluno["notas"])
        for aluno in turma
    ]

    skills = set()
    for aluno in turma:
        skills = skills | aluno["skills"]

    return {
        "alunos": len(turma),
        "media_geral": round(sum(medias) / len(medias), 2),
        "skills": skills,
    }


resumo = resumo_turma(turma)

print("Resumo da turma:")
print(resumo)


# SLIDE 9 - CONCLUSAO
divisao("SLIDE 9 - Conclusao")

print("Listas organizam sequencias.")
print("Tuplas guardam dados fixos.")
print("Conjuntos removem repeticoes.")
print("Dicionarios dao significado aos dados.")
print("Essas estruturas sao a base para analisar dados com Python.")
