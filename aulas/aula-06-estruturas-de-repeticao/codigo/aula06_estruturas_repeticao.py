"""
python3 aula6_estruturas_repeticao.py
"""


print("=" * 60)
print("AULA 6 - ESTRUTURAS DE REPETICAO")
print("=" * 60)


# ---------------------------------------------------------------------------
# 1. Por que usar repeticao?
# ---------------------------------------------------------------------------
print("\n1. POR QUE USAR REPETICAO?")

# Sem estrutura de repeticao, teriamos que escrever comandos repetidos.
# Isso deixa o codigo maior, mais cansativo de manter e mais facil de errar.
print("Sem repeticao:")
print("Estudando Python")
print("Estudando Python")
print("Estudando Python")

# Com repeticao, escrevemos a acao uma vez e mandamos o computador repetir.
# Aqui o for executa o bloco indentado 3 vezes.
print("\nCom repeticao:")
for vez in range(10):
    print("Estudando Python")


# ---------------------------------------------------------------------------
# 2. Entendendo range()
# ---------------------------------------------------------------------------
print("\n2. ENTENDENDO range()")

# A funcao range cria uma sequencia de numeros.
# Em Python, quando usamos range(4), a contagem comeca em 0 e para antes do 4.
# Por isso a saida sera: 0, 1, 2, 3.
print("Numeros gerados por range(4):")
for i in range(4):
    print(i)

# Tambem podemos informar inicio e fim.
# range(1, 6) comeca em 1 e para antes do 6.
# Entao os numeros gerados sao: 1, 2, 3, 4, 5.
print("\nNumeros gerados por range(1, 6):")
for numero in range(1, 6):
    print(numero)


# ---------------------------------------------------------------------------
# 3. Laco for
# ---------------------------------------------------------------------------
print("\n3. LACO for")

# O for e muito usado quando sabemos quantas vezes queremos repetir algo
# ou quando queremos percorrer uma sequencia de dados.
alunos = ["Ana", "Bruno", "Carlos"]

print("Lista de alunos:")
for aluno in alunos:
    # A cada repeticao, a variavel aluno recebe um nome da lista.
    print("Aluno:", aluno)


# ---------------------------------------------------------------------------
# 4. Contador com for
# ---------------------------------------------------------------------------
print("\n4. CONTADOR COM for")

# Um contador serve para controlar ou acompanhar a quantidade de repeticoes.
# Neste exemplo, usamos numero_aula para contar de 1 ate 5.
for numero_aula in range(1, 6):
    print("Aula numero:", numero_aula)


# ---------------------------------------------------------------------------
# 5. Acumulador com for
# ---------------------------------------------------------------------------
print("\n5. ACUMULADOR COM for")

# Um acumulador guarda um resultado que vai crescendo ao longo do laco.
# A variavel soma comeca em 0 porque ainda nao somamos nenhum valor.
soma = 0

# A cada repeticao, pegamos um numero da lista e somamos no acumulador.
for num in [1, 2, 3]:
    soma = soma + num

print("Soma dos numeros [1, 2, 3]:", soma)


# ---------------------------------------------------------------------------
# 6. Exemplo pratico: somar de 1 ate 5
# ---------------------------------------------------------------------------
print("\n6. EXEMPLO PRATICO: SOMAR DE 1 ATE 5")

# Este exemplo junta range, for e acumulador.
# Queremos calcular: 1 + 2 + 3 + 4 + 5.
total = 0

for numero in range(1, 6):
    # total recebe o valor antigo dele mais o numero atual.
    total = total + numero

    # Este print ajuda o aluno a enxergar o acumulador mudando.
    print("Depois de somar", numero, "o total ficou:", total)

print("Soma final:", total)


# ---------------------------------------------------------------------------
# 7. Laco while
# ---------------------------------------------------------------------------
print("\n7. LACO while")

# O while repete enquanto uma condicao for verdadeira.
# Ele e util quando nao sabemos exatamente quantas repeticoes serao necessarias.
contador = 0

while contador < 3:
    print("Contando...")

    # Esta linha e muito importante.
    # Sem atualizar o contador, a condicao contador < 3 continuaria verdadeira
    # para sempre, causando um loop infinito.
    contador = contador + 1

print("O while terminou porque contador chegou em:", contador)


# ---------------------------------------------------------------------------
# 8. Atualizacao curta: +=
# ---------------------------------------------------------------------------
print("\n8. ATUALIZACAO CURTA: +=")

# Em Python, estas duas formas fazem a mesma coisa:
# contador = contador + 1
# contador += 1
contador = 0

while contador < 3:
    print("Valor atual do contador:", contador)
    contador += 1

print("Valor final do contador:", contador)


# ---------------------------------------------------------------------------
# 9. Condicao de parada
# ---------------------------------------------------------------------------
print("\n9. CONDICAO DE PARADA")

# A condicao de parada define quando o laco deve terminar.
# Neste exemplo, a parada acontece quando tentativas chega a 3.
tentativas = 0

while tentativas < 3:
    tentativas += 1
    print("Tentativa", tentativas, "de 3")

print("Fim: a condicao tentativas < 3 deixou de ser verdadeira.")


print("\n" + "=" * 60)
print("RESUMO")
print("=" * 60)
print("for: usado para repetir com quantidade definida ou percorrer sequencias.")
print("while: usado para repetir enquanto uma condicao for verdadeira.")
print("contador: variavel usada para contar repeticoes.")
print("acumulador: variavel usada para somar ou juntar valores.")
print("condicao de parada: regra que faz o laco terminar.")
