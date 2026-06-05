# Aula 8 - Definição e Uso de Funções

# 1. Definindo uma função simples
def saudacao():
    print("Olá! Bem-vindo à nossa aula sobre funções.")

# Chamando a função
print("--- Função Simples ---")
saudacao()

# 2. Função com parâmetros
def cumprimentar(nome):
    print(f"Olá, {nome}! Tudo bem?")

print("\n--- Função com Parâmetros ---")
cumprimentar("André")
cumprimentar("Maria")

# 3. Função com retorno de valores
def somar(a, b):
    resultado = a + b
    return resultado

print("\n--- Função com Retorno ---")
total = somar(10, 5)
print(f"A soma de 10 e 5 é: {total}")

# 4. Exemplo prático: Calculando média
def calcular_media(lista_de_notas):
    soma = sum(lista_de_notas)
    quantidade = len(lista_de_notas)
    media = soma / quantidade
    return media

print("\n--- Exemplo Prático ---")
notas_turma = [8.5, 9.0, 7.5, 6.0, 10.0]
media_final = calcular_media(notas_turma)
print(f"As notas da turma são: {notas_turma}")
print(f"A média da turma é: {media_final}")
