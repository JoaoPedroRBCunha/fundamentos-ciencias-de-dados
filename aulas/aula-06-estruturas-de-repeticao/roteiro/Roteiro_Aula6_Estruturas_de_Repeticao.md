# Roteiro — Aula 6: Estruturas de Repetição

**Responsável:** Raul Nascimento Belém Pontes

---

## Descrição da aula

Nesta aula, os alunos aprenderão a automatizar tarefas repetitivas utilizando laços de repetição.

Serão exploradas as estruturas `for` e `while`, além do uso de contadores, acumuladores e condições de parada, permitindo criar programas mais dinâmicos, eficientes e capazes de resolver problemas com lógica iterativa.

---

## Objetivos de aprendizagem

- Entender a necessidade das estruturas de repetição na programação.
- Utilizar os laços `for` e `while` em Python.
- Trabalhar com contadores, acumuladores e condições de parada.
- Resolver problemas utilizando repetições e lógica iterativa.

---

## Bloco 1 — Abertura | 0:00 – 0:40

Olá!

Na aula anterior aprendemos sobre estruturas condicionais, ou seja, como fazer um programa tomar decisões utilizando `if`, `else` e `elif`.

Agora vamos aprender outro conceito muito importante na programação: as estruturas de repetição.

As estruturas de repetição permitem executar uma mesma ação várias vezes, sem precisar escrever o mesmo código repetidamente.

Imagine que você precise mostrar os números de 1 até 100 na tela.

Sem repetição, seria necessário escrever muitos comandos `print`.

Com repetição, podemos fazer isso usando poucas linhas de código.

Nesta aula, vamos aprender a utilizar os laços `for` e `while`, além de entender o uso de contadores, acumuladores e condições de parada.

---

## Bloco 2 — O que são estruturas de repetição? | 0:40 – 1:40

Estruturas de repetição são comandos que permitem executar um bloco de código várias vezes.

Elas também são chamadas de laços ou loops.

A ideia principal é repetir uma instrução enquanto uma condição for verdadeira ou durante uma determinada sequência de valores.

Por exemplo:

Imagine que queremos imprimir a mensagem "Olá, Python!" cinco vezes.

Sem repetição, faríamos assim:

```python
print("Olá, Python!")
print("Olá, Python!")
print("Olá, Python!")
print("Olá, Python!")
print("Olá, Python!")
```

Esse código funciona, mas não é eficiente.

Com uma estrutura de repetição, podemos fazer a mesma coisa de forma mais simples:

```python
for i in range(5):
    print("Olá, Python!")
```

O resultado será a mesma mensagem exibida cinco vezes.

A grande vantagem é que o código fica menor, mais organizado e mais fácil de manter.

---

## Bloco 3 — Por que usar repetição? | 1:40 – 2:40

As estruturas de repetição são importantes porque ajudam a automatizar tarefas.

Na programação, é muito comum precisarmos repetir ações, como:

- Percorrer uma lista de nomes.
- Somar vários números.
- Validar uma senha até o usuário acertar.
- Exibir uma sequência numérica.
- Calcular médias.
- Processar dados em uma tabela.

Sem repetição, teríamos que escrever muitos comandos manualmente.

Com repetição, conseguimos deixar o programa mais eficiente.

Por exemplo, imagine um sistema que precisa calcular a média de vários alunos.

Em vez de repetir o mesmo cálculo várias vezes, podemos usar um laço para percorrer as notas e realizar o cálculo automaticamente.

Por isso, os laços de repetição são fundamentais para criar programas mais dinâmicos.

---

## Bloco 4 — Laço FOR | 2:40 – 4:00

O primeiro laço que vamos estudar é o `for`.

O `for` é usado principalmente quando sabemos a quantidade de vezes que queremos repetir uma ação ou quando queremos percorrer uma sequência de dados.

A estrutura básica é:

```python
for variavel in sequencia:
    comando
```

Exemplo:

```python
for numero in range(1, 6):
    print(numero)
```

Nesse exemplo, o Python vai exibir os números de 1 até 5.

A função `range(1, 6)` cria uma sequência que começa em 1 e vai até 5.

É importante observar que o último número, nesse caso o 6, não entra na sequência.

A variável `numero` recebe um valor diferente a cada repetição.

Na primeira repetição, ela vale 1.

Na segunda, vale 2.

E assim por diante, até chegar ao valor 5.

O `for` é muito utilizado quando precisamos repetir algo por uma quantidade definida de vezes.

---

## Bloco 5 — Usando FOR com listas | 4:00 – 5:00

Além de usar o `for` com a função `range`, também podemos utilizar esse laço para percorrer listas.

Uma lista é uma coleção de valores.

Por exemplo:

```python
nomes = ["Ana", "João", "Maria"]

for nome in nomes:
    print(nome)
```

Nesse exemplo, o Python percorre a lista `nomes`.

A cada repetição, a variável `nome` recebe um item da lista.

Primeiro, recebe `"Ana"`.

Depois, recebe `"João"`.

Por fim, recebe `"Maria"`.

Esse tipo de repetição é muito comum em programas que trabalham com vários dados, como nomes, notas, produtos, idades ou valores de uma tabela.

O `for` facilita bastante o processamento de coleções de informações.

---

## Bloco 6 — Laço WHILE | 5:00 – 6:30

Agora vamos conhecer o laço `while`.

A palavra `while` significa "enquanto".

Esse laço executa um bloco de código enquanto uma condição for verdadeira.

A estrutura básica é:

```python
while condicao:
    comando
```

Exemplo:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1
```

Nesse exemplo, criamos uma variável chamada `contador` com valor inicial 1.

O laço `while` verifica se o contador é menor ou igual a 5.

Enquanto essa condição for verdadeira, o número será exibido na tela.

Depois disso, o contador é aumentado em 1.

Quando o contador passa a valer 6, a condição se torna falsa e o laço é encerrado.

O `while` é muito usado quando não sabemos exatamente quantas vezes a repetição irá acontecer.

Por exemplo, quando queremos repetir uma ação até que o usuário digite uma informação correta.

---

## Bloco 7 — Condição de parada e loop infinito | 6:30 – 7:40

Ao usar o `while`, precisamos ter muito cuidado com a condição de parada.

A condição de parada é o que define quando o laço deve terminar.

Se ela nunca for atingida, o programa pode entrar em um loop infinito.

Um loop infinito acontece quando o código fica repetindo para sempre.

Veja um exemplo problemático:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Nesse caso, o contador começa em 1, mas nunca é atualizado.

Então a condição `contador <= 5` será sempre verdadeira.

Isso faz com que o programa fique preso no laço.

Para corrigir, precisamos atualizar o contador dentro do `while`:

```python
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1
```

Agora, a cada repetição, o contador aumenta.

Quando ele passar de 5, o laço será encerrado.

Por isso, sempre que usar `while`, lembre-se de garantir que a condição possa se tornar falsa em algum momento.

---

## Bloco 8 — Contadores | 7:40 – 8:40

Um contador é uma variável usada para contar repetições ou controlar a execução de um laço.

Normalmente, o contador começa com um valor inicial e é atualizado a cada repetição.

Exemplo:

```python
contador = 1

while contador <= 3:
    print("Repetição número:", contador)
    contador = contador + 1
```

Nesse exemplo, a variável `contador` controla quantas vezes o laço será executado.

Também podemos escrever a atualização de forma mais curta:

```python
contador += 1
```

Essa linha significa a mesma coisa que:

```python
contador = contador + 1
```

Contadores são muito utilizados quando precisamos saber quantas vezes algo aconteceu.

Por exemplo:

- Contar quantos alunos foram aprovados.
- Contar quantos produtos existem em uma lista.
- Contar quantas tentativas um usuário realizou.

---

## Bloco 9 — Acumuladores | 8:40 – 9:50

Um acumulador é uma variável usada para guardar um valor que vai sendo atualizado ao longo das repetições.

Ele é muito usado para somar valores.

Por exemplo, vamos somar os números de 1 até 5:

```python
total = 0

for numero in range(1, 6):
    total = total + numero

print("Soma final:", total)
```

Nesse exemplo, a variável `total` começa com o valor 0.

A cada repetição, o valor de `numero` é somado ao `total`.

O processo acontece assim:

- Primeiro, soma 1.
- Depois, soma 2.
- Depois, soma 3.
- Depois, soma 4.
- Por fim, soma 5.

No final, o resultado será:

```text
Soma final: 15
```

Esse tipo de lógica é muito comum para calcular totais, médias, pontuações e relatórios.

---

## Bloco 10 — Exemplo prático com média | 9:50 – 11:20

Agora vamos juntar os conceitos em um exemplo prático.

Imagine que queremos calcular a média de três notas.

Podemos usar um laço `for` para repetir a leitura das notas e um acumulador para somar os valores.

```python
soma = 0

for i in range(3):
    nota = float(input("Digite uma nota: "))
    soma = soma + nota

media = soma / 3

print("Média:", media)
```

Nesse exemplo, a variável `soma` é o acumulador.

Ela começa com o valor 0.

A cada repetição, o usuário digita uma nota, e essa nota é somada à variável `soma`.

Depois que o laço termina, calculamos a média dividindo a soma por 3.

Esse exemplo mostra como as estruturas de repetição ajudam a resolver problemas de forma mais organizada.

Em vez de escrever três comandos separados para cada nota, usamos um laço para repetir a mesma ação.

---

## Bloco 11 — Quando usar FOR e quando usar WHILE? | 11:20 – 12:30

Uma dúvida comum é saber quando usar `for` e quando usar `while`.

De forma simples:

Use `for` quando você sabe a quantidade de repetições ou quando deseja percorrer uma sequência.

Por exemplo:

```python
for numero in range(1, 6):
    print(numero)
```

Nesse caso, sabemos que queremos percorrer os números de 1 até 5.

Use `while` quando a repetição depende de uma condição e você não sabe exatamente quantas vezes ela irá acontecer.

Por exemplo:

```python
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso liberado")
```

Nesse caso, o programa continua pedindo a senha até que o usuário digite o valor correto.

Pode acontecer na primeira tentativa ou depois de várias tentativas.

Por isso, o `while` é mais adequado.

---

## Bloco 12 — Encerramento | 12:30 – 13:20

Vamos revisar o que aprendemos nesta aula.

Vimos que estruturas de repetição permitem executar um bloco de código várias vezes.

Aprendemos que o `for` é muito útil quando sabemos a quantidade de repetições ou quando queremos percorrer uma sequência de dados.

Também vimos que o `while` executa um bloco enquanto uma condição for verdadeira.

Além disso, estudamos contadores, acumuladores e condições de parada.

Esses conceitos são fundamentais para criar programas mais eficientes, porque permitem automatizar tarefas repetitivas e resolver problemas usando lógica iterativa.

Na próxima aula, vamos avançar para estruturas de dados, aprendendo como armazenar e organizar vários valores em Python.

Até a próxima aula!
