# Roteiro — Aula 5: Estruturas Condicionais

**Responsável:** Felipe Ramalho Perdigão

---

## Descrição da aula

Nesta aula, os alunos aprenderão como os programas podem tomar decisões a partir de condições lógicas.

Serão apresentados os conceitos de comparação, operadores relacionais e operadores lógicos aplicados às estruturas condicionais do Python, permitindo criar programas capazes de executar diferentes ações dependendo da situação analisada.

A aula abordará as estruturas `if`, `else` e `elif`, além da utilização de operadores lógicos para combinar condições e resolver problemas simples envolvendo tomada de decisão.

---

## Objetivos de aprendizagem

- Compreender o funcionamento das estruturas condicionais em Python.
- Utilizar operadores relacionais e lógicos em expressões condicionais.
- Aplicar as estruturas `if`, `elif` e `else`.
- Desenvolver programas simples com tomada de decisão.

---

## Bloco 1 — Abertura | 0:00 – 0:40

Olá!

Na aula anterior aprendemos sobre variáveis, tipos de dados e operadores.

Agora vamos dar um passo muito importante na programação: aprender como fazer o programa tomar decisões.

Pense em situações do dia a dia.

Se estiver chovendo, levamos um guarda-chuva.

Se a nota for maior ou igual a sete, o aluno é aprovado.

Se a idade for maior ou igual a dezoito anos, a pessoa é considerada maior de idade.

Perceba que todas essas situações dependem de uma condição.

Da mesma forma, os programas também podem tomar decisões utilizando estruturas condicionais.

Nesta aula vamos aprender como utilizar as estruturas `if`, `else` e `elif` para criar programas mais inteligentes e interativos.

---

## Bloco 2 — O que são estruturas condicionais? | 0:40 – 1:40

As estruturas condicionais permitem que um programa execute diferentes ações dependendo de uma condição.

Em outras palavras, elas permitem que o computador escolha um caminho de execução.

Por exemplo:

Imagine um sistema escolar.

Se a média do aluno for maior ou igual a sete, ele será aprovado.

Caso contrário, será reprovado.

Essa decisão pode ser representada da seguinte forma:

```python
media = 8

if media >= 7:
    print("Aprovado")
```

Nesse exemplo, o Python verifica se a média é maior ou igual a sete.

Se a condição for verdadeira, a mensagem será exibida.

Caso contrário, nada acontecerá.

As estruturas condicionais são fundamentais porque permitem criar programas que reagem a diferentes situações.

---

## Bloco 3 — Relembrando operadores relacionais | 1:40 – 2:40

Antes de utilizar estruturas condicionais, precisamos lembrar dos operadores relacionais.

São eles que permitem fazer comparações.

Os principais operadores relacionais são:

```text
==  igual a
!=  diferente de
>   maior que
<   menor que
>=  maior ou igual a
<=  menor ou igual a
```

Exemplo:

```python
idade = 18

print(idade >= 18)
```

Nesse caso, o Python verifica se a idade é maior ou igual a dezoito.

Como a condição é verdadeira, o resultado será:

```python
True
```

As estruturas condicionais utilizam exatamente esse tipo de comparação para decidir qual ação executar.

---

## Bloco 4 — Estrutura IF | 2:40 – 4:00

A estrutura condicional mais simples é o `if`.

A palavra `if` significa "se".

Sua função é executar um bloco de código apenas quando uma condição for verdadeira.

A estrutura é a seguinte:

```python
if condicao:
    comando
```

Exemplo:

```python
idade = 20

if idade >= 18:
    print("Você é maior de idade")
```

Nesse exemplo, o Python verifica a condição:

```python
idade >= 18
```

Como a condição é verdadeira, a mensagem é exibida.

Agora observe:

```python
idade = 15

if idade >= 18:
    print("Você é maior de idade")
```

Nesse caso a condição é falsa.

Por isso, nenhuma mensagem será exibida.

O bloco dentro do `if` só é executado quando a condição for verdadeira.

---

## Bloco 5 — Estrutura ELSE | 4:00 – 5:20

Mas e se quisermos executar uma ação quando a condição for falsa?

Para isso utilizamos o `else`.

A palavra `else` significa "senão".

Exemplo:

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

O Python primeiro verifica a condição.

Se ela for verdadeira, executa o bloco do `if`.

Caso contrário, executa o bloco do `else`.

Nesse exemplo, como a idade é quinze anos, a saída será:

```text
Menor de idade
```

Assim conseguimos tratar tanto situações verdadeiras quanto falsas.

---

## Bloco 6 — Estrutura ELIF | 5:20 – 6:50

Em alguns casos precisamos verificar mais de duas possibilidades.

Para isso utilizamos o `elif`.

A palavra `elif` significa "senão se".

Exemplo:

```python
nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

Nesse caso:

- Se a nota for maior ou igual a sete, o aluno está aprovado.
- Se não for, o Python verifica a segunda condição.
- Se a nota for maior ou igual a cinco, o aluno fica em recuperação.
- Caso nenhuma condição seja verdadeira, ele será reprovado.

O Python verifica as condições de cima para baixo até encontrar uma condição verdadeira.

---

## Bloco 7 — Operadores lógicos em condições | 6:50 – 8:00

Também podemos combinar várias condições utilizando operadores lógicos.

Os principais são:

```python
and
or
not
```

Exemplo com `and`:

```python
idade = 20
possui_cnh = True

if idade >= 18 and possui_cnh:
    print("Pode dirigir")
```

Nesse caso, as duas condições precisam ser verdadeiras.

A pessoa precisa ter dezoito anos ou mais e também possuir carteira de habilitação.

Exemplo com `or`:

```python
tem_cartao = False
tem_pix = True

if tem_cartao or tem_pix:
    print("Pagamento permitido")
```

Nesse caso, basta uma das condições ser verdadeira.

---

## Bloco 8 — Exemplo prático completo | 8:00 – 9:20

Agora vamos juntar tudo em um exemplo simples.

Imagine um sistema de login.

```python
senha = "python123"

if senha == "python123":
    print("Acesso liberado")
else:
    print("Senha incorreta")
```

O programa compara a senha digitada com a senha correta.

Se elas forem iguais, o acesso é liberado.

Caso contrário, o sistema informa que a senha está incorreta.

Esse é um exemplo simples, mas mostra como as estruturas condicionais são utilizadas em sistemas reais.

---

## Bloco 9 — Encerramento | 9:20 – 10:00

Vamos revisar o que aprendemos.

Nesta aula vimos que as estruturas condicionais permitem que os programas tomem decisões.

Aprendemos a utilizar:

- `if` para executar ações quando uma condição é verdadeira.
- `else` para executar ações quando a condição é falsa.
- `elif` para verificar múltiplas condições.
- Operadores relacionais para realizar comparações.
- Operadores lógicos para combinar condições.

Esses conceitos são fundamentais para criar programas capazes de responder a diferentes situações.

Na próxima etapa dos estudos, veremos como repetir ações automaticamente utilizando estruturas de repetição.

Até a próxima aula!
