# Algoritmo de Rabin Karp

## Introdução

Você já sabe um jeito básico para procurar padrão em strings, vamos relembrar:

func1(string padrao, string text):  
 for i in text:
LÉOZINHO JR É PATETICO
(terminar codigo)

Já sabemos que essa maneira não é ideal pois tem complexidade $$O(nm)$$ e como vocês viram há outras maneiras mais eficientes de solucionar este problema, vamos implementar mais uma forma.  

## Questão 1

Antes de iniciarmos com o algoritmo, é importante falarmos um pouco sobre _hashing_, pois ele é essêncial para o funcionamento dessa busca. Apenas como aquecimento, discuta com seus colegas de bancada se algum de vocês ja ouviu falar sobre este tema.  
Coisa rapida, levem cerca de 2 minutos e sigam em frente.

###

## Hashing

_Hashing_ é um processo que gera uma saída de um valor a partir de uma entrada com tamanho variável. Essa entrada pode ser tanto números quanto caracteres.O valor da saída é conhecido como _Hash Value_ e para chegarmos nesse valor utilizamos uma função, chamada de _Hashing function_. Essa função pode ser implementada de diversas maneiras, porem mais para frente você vai entender o porquê o tipo de implementação é importante.

Para calcular um _Hash Value_ é utilizado os valores da tabela ASCII respectivos para cada caracter. Você pode acessar a tabela ASCII [aqui](https://www.insper.edu.br/).

## Questão 2

Uma maneira para se obter o _hash Value_ é simplesmente somar o valor da tabela ASCII referente a cada caracter. Vamos ver se você entendeu? Calcule o _hash Value_ da palavra `HASH`.

###

    72 + 65 + 72 + 83 = 292

## Questão 3

Essa _Hashing function_ function pode, eventualmente, gerar um problema. Você consegue pensar em qual é? Reflita um pouquinho antes de continuar.  
Dica: calcule o _hash value_ de `CPDM`.

###

## Colisão

Entendeu? O problema dessa função é relacionado ao que chamamos de _colisão_. Uma colisão ocorre quando duas ou mais entradas têm o mesmo hash value. **Todas** as funções têm chances de ocorrer colisão, mas algumas funções tem uma menor probabilidade do que outras. Uma _boa_ hash function diminui ao máximo o número de colisões.  
Nesta aula utilizaremos a seguinte lei, para a função de hashing:

$$Value = R.X_1^{N-1} + R.X_2^{N-1} + R.X_3^{N-2} + ...  + R.X_N^0$$

Onde:

- N é a quantidade de caracteres do padrão calculado.
- X é o valor do caracter na tabela ASCII
- R é a quantidade de caracteres do alfabeto utilizado, por exemplo R = 256 para o alfabeto ASCII estendido.

## ??

Agora que _hash_ é algo além de uma palavra legal da computação, podemos seguir com o algoritimo desse encontro. O Rabin-Karp consiste em iterar com esse hash value sobre o hash do texto inteiro, como exemplificado no exemplo abaixo:

![simulacao1](simulacao1.gif)

compara sem utilizar rolling hash
complexidade ruim

        FAZER CODIGO SEM ROLLING HASH CALCULANDO O HASH DE CADA CARACTER
        A LÉO JR É PATÉTICO

Esse código ainda tem uma complexidade ruim de $$O(nm)$$ pois ainda é necessário acessar vários caracteres múltiplas vezes para pegar o seu valor. Como é possível observar na simulação acima, primeiro é calculado o valor de `ADA`, na proxima iteração, é calcular do valor de `DAC`, porém, o valor de `DA` que já foi calculado na primeira iteração, é recalculado para a segunda.  
Você consegue pensar em algum jeito de contornar isso?

###

## Rolling Hash

_Rolling Hash_ é um tipo de função que consiste em manter a maior parte dos números já calculados, evitando o desperdicio de tempo e memoria que seria recalcular. Por exemplo, após o primeiro cálculo do valor de Hash, basta subtrair o valor do primeiro caracter comparado e adicionar o do proximo caracter.

![simulacao2](simulacao2.gif)
