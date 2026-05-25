# Roteiro — Aula 4: Tipos Básicos e Variáveis

**Responsável:** João Pedro Ribeiro Cunha

---

## Descrição da aula

Nesta aula, os alunos aprenderão os conceitos iniciais da programação em Python por meio do estudo dos tipos básicos de dados e do uso de variáveis. Serão apresentados os principais tipos, como números inteiros, números decimais, textos e valores booleanos, além da forma correta de declarar, armazenar e manipular informações em variáveis.

A aula também abordará expressões e operadores aritméticos, relacionais e lógicos, permitindo que os alunos realizem operações básicas e compreendam como esses recursos são utilizados na construção de programas simples em Python.

---

## Objetivos de aprendizagem

- Compreender os tipos de dados básicos do Python.
- Declarar e utilizar variáveis em Python.
- Aplicar expressões e operadores nas operações básicas.

---

## Bloco 1 — Abertura | 0:00 – 0:30

Olá! Nesta aula, vamos aprender conceitos fundamentais para começar a programar em Python: variáveis, tipos básicos de dados e operadores.

Esses conteúdos são a base de praticamente qualquer programa, porque todo código precisa armazenar informações, manipular valores e realizar operações.

Ao longo da aula, vamos entender como criar variáveis, quais são os principais tipos de dados do Python e como utilizar operadores aritméticos, relacionais e lógicos. Vamos começar.

---

## Bloco 2 — O que são variáveis? | 0:30 – 1:30

Antes de falar sobre tipos de dados, precisamos entender o que são variáveis.

Uma variável é um espaço na memória utilizado para armazenar um valor.

Podemos imaginar uma variável como uma caixinha que recebe um nome. Dentro dessa caixinha, podemos guardar uma informação, como um nome, uma idade, uma nota ou uma resposta verdadeira ou falsa.

Por exemplo:

```python
nome = "João"
idade = 20
altura = 1.75
estudante = True
```

Nesse exemplo, criamos quatro variáveis.

A variável `nome` guarda um texto.  
A variável `idade` guarda um número inteiro.  
A variável `altura` guarda um número decimal.  
E a variável `estudante` guarda um valor lógico, verdadeiro ou falso.

Ou seja, as variáveis servem para armazenar informações que poderão ser usadas durante a execução do programa.

---

## Bloco 3 — Como definir variáveis em Python | 1:30 – 2:30

Para definir uma variável em Python, usamos o nome da variável, o sinal de igual e o valor que queremos armazenar.

A estrutura é assim:

```python
nome_da_variavel = valor
```

Por exemplo:

```python
curso = "Ciência de Dados"
ano = 2026
media = 8.5
aprovado = True
```

O sinal de igual, nesse caso, não significa uma comparação matemática. Ele significa atribuição.

Ou seja, quando escrevemos:

```python
idade = 20
```

Estamos dizendo para o Python: guarde o valor `20` dentro da variável chamada `idade`.

Em Python, não precisamos informar o tipo da variável antes de criar ela. A própria linguagem identifica automaticamente o tipo de acordo com o valor informado.

Por exemplo:

```python
nome = "Maria"
idade = 25
preco = 19.90
ativo = False
```

Esse comportamento é chamado de tipagem dinâmica.

Isso significa que a variável pode receber diferentes tipos de valores ao longo do programa. Por exemplo:

```python
valor = 10
print(valor)

valor = "Python"
print(valor)
```

Primeiro, a variável `valor` recebe um número inteiro. Depois, recebe um texto.

Embora Python permita isso, é importante manter organização e clareza, para que o código não fique confuso.

---

## Bloco 4 — Regras para criar variáveis | 2:30 – 3:30

Ao criar variáveis em Python, precisamos seguir algumas regras.

O nome da variável pode conter letras, números e underline, mas não pode começar com número.

Exemplos corretos:

```python
nome = "Ana"
idade_usuario = 30
nota1 = 8.5
```

Exemplos incorretos:

```python
1nota = 8.5
nome completo = "Ana Silva"
valor-total = 100
```

Também é importante escolher nomes claros e descritivos.

Por exemplo, em vez de escrever:

```python
x = 25
```

É melhor escrever:

```python
idade = 25
```

Assim, o código fica mais fácil de entender.

Em Python, a convenção mais comum é usar letras minúsculas e separar palavras com underline.

Exemplo:

```python
nome_completo = "João Pedro"
valor_total = 150.75
```

Essa forma de escrita é chamada de `snake_case` e é bastante utilizada em Python.

---

## Bloco 5 — O que são tipos de dados? | 3:30 – 4:20

Agora que já sabemos o que são variáveis, podemos entender os tipos de dados.

Em Python, todo valor armazenado em uma variável possui um tipo.

O tipo de dado representa a natureza daquela informação.

Por exemplo:

```python
idade = 20
nome = "João"
altura = 1.75
estudante = True
```

Cada variável armazena um tipo diferente de valor.

A variável `idade` armazena um número inteiro.  
A variável `nome` armazena um texto.  
A variável `altura` armazena um número decimal.  
E a variável `estudante` armazena um valor lógico.

Os principais tipos básicos que vamos estudar são:

- `int`, para números inteiros.
- `float`, para números decimais.
- `str`, para textos.
- `bool`, para verdadeiro ou falso.

Esses tipos aparecem constantemente em programas simples e também em projetos maiores de Ciência de Dados.

---

## Bloco 6 — Tipo int: números inteiros | 4:20 – 5:10

O primeiro tipo básico é o `int`.

O `int` representa números inteiros, ou seja, números sem parte decimal.

Exemplos de valores inteiros são:

```python
idade = 20
quantidade = 5
ano = 2026
```

Nesse caso, a variável `idade` armazena o valor `20`, `quantidade` armazena o valor `5` e `ano` armazena o valor `2026`.

Esse tipo é muito utilizado quando trabalhamos com contagens, idades, quantidades, anos, códigos numéricos e outras informações que não precisam de casas decimais.

Podemos verificar o tipo de uma variável utilizando a função `type()`:

```python
idade = 20
print(type(idade))
```

A saída será:

```python
<class 'int'>
```

Isso mostra que o valor armazenado é do tipo inteiro.

---

## Bloco 7 — Tipo float: números decimais | 5:10 – 6:00

O segundo tipo é o `float`.

O `float` representa números com casas decimais.

Em Python, utilizamos ponto no lugar da vírgula para representar números decimais.

Por exemplo:

```python
altura = 1.75
preco = 29.90
media = 8.5
```

Esse tipo é muito usado para representar valores como preços, médias, medidas, notas, porcentagens e resultados de cálculos.

Por exemplo:

```python
nota1 = 8.0
nota2 = 7.5

media = (nota1 + nota2) / 2

print(media)
```

Nesse caso, o Python soma as duas notas e divide por 2, gerando uma média com valor decimal.

---

## Bloco 8 — Tipo str: textos | 6:00 – 7:00

O terceiro tipo é o `str`.

O `str` é utilizado para armazenar textos, também chamados de strings.

Em Python, textos devem ser escritos entre aspas simples ou aspas duplas.

Por exemplo:

```python
nome = "João"
curso = "Ciência de Dados"
linguagem = 'Python'
```

Tanto aspas simples quanto aspas duplas funcionam. O importante é abrir e fechar o texto com o mesmo tipo de aspas.

Strings são usadas para nomes, mensagens, endereços, descrições, e-mails e qualquer informação textual.

Também podemos juntar textos usando o operador de soma, que nesse caso funciona como concatenação.

Exemplo:

```python
nome = "João"
mensagem = "Olá, " + nome

print(mensagem)
```

A saída será:

```text
Olá, João
```

Ou seja, o Python juntou os textos e formou uma mensagem completa.

---

## Bloco 9 — Tipo bool: verdadeiro ou falso | 7:00 – 7:50

O quarto tipo básico é o `bool`.

O `bool` representa valores lógicos, ou seja, verdadeiro ou falso.

Em Python, usamos:

```python
True
False
```

Com a primeira letra maiúscula.

Exemplo:

```python
ativo = True
maior_de_idade = False
```

Esse tipo é muito importante para decisões dentro dos programas.

Por exemplo, podemos usar um valor booleano para indicar se um usuário está ativo, se uma compra foi aprovada, se uma senha está correta ou se uma condição foi atendida.

Mais adiante, quando estudarmos estruturas condicionais, como `if` e `else`, os valores booleanos serão fundamentais.

---

## Bloco 10 — Operadores aritméticos | 7:50 – 9:10

Depois de entender variáveis e tipos de dados, podemos trabalhar com operadores.

Os operadores aritméticos são usados para realizar cálculos matemáticos.

Os principais são:

```text
+   soma
-   subtração
*   multiplicação
/   divisão
//  divisão inteira
%   resto da divisão
**  potência
```

Exemplo:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Nesse exemplo:

- A soma retorna `13`.
- A subtração retorna `7`.
- A multiplicação retorna `30`.
- A divisão retorna `3.333...`.
- A divisão inteira retorna `3`.
- O resto da divisão retorna `1`.
- A potência retorna `1000`.

Esses operadores são muito utilizados em cálculos simples, médias, porcentagens e fórmulas em geral.

---

## Bloco 11 — Operadores relacionais | 9:10 – 10:20

Os operadores relacionais são usados para comparar valores.

Eles retornam sempre um resultado booleano: `True` ou `False`.

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

print(idade == 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
```

A primeira comparação verifica se a idade é igual a `18`.

A segunda verifica se a idade é maior que `18`.

A terceira verifica se a idade é menor que `18`.

A quarta verifica se a idade é maior ou igual a `18`.

Esse tipo de comparação será muito importante quando formos criar programas que tomam decisões.

Por exemplo: verificar se uma pessoa pode votar, se um aluno foi aprovado ou se um produto está disponível em estoque.

---

## Bloco 12 — Operadores lógicos | 10:20 – 11:30

Os operadores lógicos são usados para combinar condições.

Os principais operadores lógicos em Python são:

```python
and
or
not
```

O operador `and` retorna `True` somente quando todas as condições são verdadeiras.

Exemplo:

```python
idade = 20
tem_documento = True

print(idade >= 18 and tem_documento == True)
```

Nesse caso, o resultado será `True`, porque a idade é maior ou igual a `18` e a pessoa tem documento.

O operador `or` retorna `True` quando pelo menos uma condição é verdadeira.

Exemplo:

```python
tem_cartao = False
tem_pix = True

print(tem_cartao or tem_pix)
```

O resultado será `True`, porque pelo menos uma das condições é verdadeira.

Já o operador `not` inverte o valor lógico.

Exemplo:

```python
ativo = True

print(not ativo)
```

A saída será:

```python
False
```

Esses operadores são muito usados em validações e regras de negócio dentro dos programas.

---

## Bloco 13 — Exemplo prático | 11:30 – 12:50

Agora vamos juntar os conceitos em um exemplo simples.

Imagine que queremos calcular a média de um aluno e verificar se ele foi aprovado.

```python
nome = "Carlos"
nota1 = 8.0
nota2 = 7.0

media = (nota1 + nota2) / 2

aprovado = media >= 7

print("Aluno:", nome)
print("Média:", media)
print("Aprovado:", aprovado)
```

Nesse exemplo, usamos:

- Uma variável do tipo `str` para armazenar o nome.
- Variáveis do tipo `float` para armazenar as notas.
- Uma expressão aritmética para calcular a média.
- Um operador relacional para verificar se a média é maior ou igual a `7`.
- Uma variável booleana para armazenar o resultado da aprovação.

Esse é um exemplo simples, mas já mostra como variáveis, tipos de dados e operadores trabalham juntos dentro de um programa.

---

## Bloco 14 — Encerramento | 12:50 – 13:20

Resumindo: nesta aula, aprendemos o que são variáveis, como definir variáveis em Python e quais regras devemos seguir ao nomeá-las.

Também vimos os principais tipos básicos do Python: `int`, `float`, `str` e `bool`.

Além disso, aprendemos a aplicar operadores aritméticos, relacionais e lógicos em operações básicas.

Esses conceitos são fundamentais para continuar aprendendo programação, porque eles aparecem em praticamente todos os códigos.

Na próxima aula, vamos avançar para as estruturas condicionais, aprendendo como fazer o programa tomar decisões com base em condições. Até lá!
