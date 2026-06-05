# Roteiro — Aula 8: Definição e Uso de Funções

---

## Bloco 1 — Abertura | 0:00 – 0:30

Olá! Nas últimas aulas você aprendeu sobre os tipos de dados e como usar estruturas de repetição e condicionais. Hoje, vamos dar um passo essencial para tornar seu código profissional: vamos falar sobre Funções.

Nesta aula, você vai aprender como organizar e reaproveitar seu código através da definição de funções em Python.

---

## Bloco 2 — O que é uma Função e por que usamos? | 0:30 – 1:45

Uma função é como uma pequena máquina: você fornece alguns dados (entradas), ela processa esses dados e te devolve um resultado (saída). 

Por que isso é importante? Imagine que você precise calcular a média de vários conjuntos de dados diferentes. Em vez de escrever o mesmo código de soma e divisão várias vezes, você cria uma função chamada `calcular_media` e apenas chama essa função sempre que precisar.

Isso traz duas vantagens enormes: 
1. **Reutilização**: você escreve o código uma vez e usa quantas vezes quiser.
2. **Organização (Modularização)**: seu programa fica dividido em pequenas partes com nomes claros, facilitando muito a leitura e a manutenção.

---

## Bloco 3 — Criando Funções com `def` | 1:45 – 3:00

No Python, usamos a palavra reservada `def` para declarar uma função. A estrutura é muito simples: escrevemos `def`, o nome da função seguido de parênteses e dois pontos. Tudo que estiver identado (com espaço) abaixo disso fará parte da função.

Por exemplo:
```python
def saudacao():
    print("Olá! Bem-vindo à aula!")
```
Se você rodar só isso, nada vai aparecer na tela. A função só existe, mas precisa ser **chamada** para funcionar. Para isso, basta escrever o nome dela com parênteses fora do bloco: `saudacao()`.

---

## Bloco 4 — Trabalhando com Parâmetros | 3:00 – 4:15

E como passamos dados para dentro dessa "máquina"? Usamos os parâmetros. Dentro dos parênteses da definição da função, colocamos variáveis que vão receber esses dados.

Por exemplo, podemos fazer:
```python
def cumprimentar(nome):
    print(f"Olá, {nome}! Tudo bem?")
```
Agora, ao chamar a função, precisamos entregar um valor para `nome`, assim: `cumprimentar("André")`. O código saberá que "André" deve ser usado onde estiver a variável `nome`.

---

## Bloco 5 — Valores de Retorno (`return`) | 4:15 – 5:30

Muitas vezes, não queremos que a função apenas imprima algo na tela, queremos que ela calcule um valor para podermos usar em outra parte do código. Para isso usamos a palavra `return`.

Por exemplo:
```python
def somar(a, b):
    resultado = a + b
    return resultado
```
Com o `return`, o valor calculado é devolvido, e você pode guardá-lo numa variável: `total = somar(10, 5)`. Em Ciência de Dados, o tempo inteiro criamos funções para processar e retornar dados limpos ou métricas calculadas.

---

## Bloco 6 — Mão na Massa | 5:30 – 6:30

Agora é sua vez! Abra seu VSCode, crie um arquivo e pratique.
1. Crie uma função simples que imprima uma mensagem na tela.
2. Crie uma função que receba dois parâmetros matemáticos e retorne o resultado de uma multiplicação.
3. Se quiser um desafio: crie uma função que receba uma lista de números e retorne a média deles.

O arquivo com os exemplos feitos aqui em aula já está na pasta "codigo" para você usar como referência.

---

## Bloco 7 — Encerramento | 6:30 – 7:00

Parabéns! Hoje você descobriu como organizar e otimizar seus programas usando funções, parâmetros e retornos.

Este conceito vai acompanhar você ao longo de toda a sua jornada em programação e Ciência de Dados. Quanto mais modularizado for seu código, mais fácil será de entender e melhorar. Continue praticando e até a próxima aula!
