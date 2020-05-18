# Algoritmo de Rabin Karp

## Introdução

Você já sabe um jeito básico para procurar padrão em strings, vamos relembrar:  
    
    def stringMatching(text, pattern):
        indexes = []
        for i in range(len(text)):
            if text[i:(len(pattern)+i)] == pattern:
                indexes.append(i)
        return indexes


Já sabemos que essa maneira não é ideal pois tem complexidade $$O(nm)$$ e como vocês viram há outras maneiras mais eficientes de solucionar este problema, vamos implementar mais uma forma.  

## Questão 1

Antes de iniciarmos com o algoritmo, é importante falarmos um pouco sobre **_hashing_**, pois ele é essêncial para o funcionamento dessa busca. Apenas como aquecimento, discuta com seus colegas se algum de vocês ja ouviu falar sobre este tema.  
Coisa rapida, levem cerca de 2 minutos e sigam em frente.

###

## Hashing

**_Hashing_** é um processo que gera uma saída de um valor a partir de uma entrada com tamanho variável. Essa entrada pode ser tanto números quanto caracteres. O valor da saída é conhecido como **_Hash Value_** e para chegarmos nesse valor utilizamos uma função, chamada de _Hashing function_. Essa função pode ser implementada de diversas maneiras, porém mais para frente você vai entender o porquê o tipo de implementação é importante.

Para calcular um **_Hash Value_** é utilizado os valores da tabela ASCII respectivos para cada caracter. Você pode acessar a tabela ASCII [aqui](https://jeffersonpalheta.files.wordpress.com/2017/09/ascii.png).

## Questão 2

Uma maneira para se obter o _hash Value_ é simplesmente somar o valor da tabela ASCII referente a cada caracter. Vamos ver se você entendeu? Calcule o _hash Value_ da palavra `HASH`.

###

    72 + 65 + 72 + 83 = 292

## Questão 3
Agora que vc entendeu como funciona, tente pensar em como implementar essas mudanças no código que você viu acima para comparar os _hash Value_ ao invés de comparar caracter por caracter.

###

Você deve ter chegado em algo parecido com isso:

    def stringSearchHash(text, pattern):
        indexes = []
        
        pattern_value= 0
        for character in pattern:
            pattern_value += ord(character)
        for i in range(len(text)):
            j=i
            text_value = 0
            if (i+len(pattern)>len(text)):
                break
            while(j<i+len(pattern)):
                text_value+=ord(text[j])
                j+=1
            if (text_value==pattern_value):
                indexes.append(i)
        
        return indexes

Mas, ainda temos um problema. Esse código ainda tem uma complexidade de $$O(nm)$$. Para solucionar isso iremos utilizar um método chamado _Rolling Hash_.

## Rolling Hash

A correção para melhorar a complexidade é a aplicação do _Rolling Hash_, que consiste em manter a maior parte dos números já calculados, evitando o desperdício de tempo e memória que seria recalculá-los. Por exemplo, após o primeiro cálculo do valor de Hash, basta subtrair o valor do primeiro carácter comparado e adicionar o do próximo carácter.
Esta função pode ser visualizada na animação abaixo:  

![simulacao2](simulacao2.gif)


**faz questao aqui pra pessoa tentar implementar o codigo?
      
      
    def RollingHash(text, pattern):
        indexes = []
            
        m = len(text)
        n = len(pattern)

        text_value =0
        pattern_value = 0

        for i in range(len(pattern)):
            pattern_value+= ord(pattern[i])
            text_value += ord(text[i])
        if (text_value==pattern_value):
            indexes.append(i) 
        for i in range(n,len(text)):
            text_value = text_value + ord(text[i]) - ord(text[i-3])
            if (text_value==pattern_value):
                indexes.append(i)
        return indexes;



          
![complexidade](complexidade.png)   //achar o lugar dessa imagem

## Questão 5  

Qual é a complexidade desse código? 



## Questão 4

Essa _Hashing function_ pode, eventualmente, gerar um problema. Você consegue pensar em qual é? Reflita um pouquinho antes de continuar.  
>DICA:   
>Simule as funções acima com as entradas:  
>text: "O MARCELO HASHIMOTO ESTÁ INDO NA PADARIA PDCM, ALGÚEM QUER ALGO?"  
>pattern: "HASH"  

###

## Colisão

Notou algum problema? Esse caso é o que chamamos de _colisão_. Uma colisão ocorre quando duas ou mais entradas têm o mesmo hash value. No exemplo acima, tanto `HASH` como `PDCM` tem o mesmo hash value. **Todas** as funções têm chances de ocorrer colisão, mas algumas funções tem uma menor probabilidade do que outras. Uma _boa_ hash function diminui ao máximo o número de colisões.  
Nesta aula utilizaremos a seguinte lei para a função de hashing:

$$Value = R.X_1^{N-1} + R.X_2^{N-1} + R.X_3^{N-2} + ...  + R.X_N^0$$

Onde:

- N é a quantidade de caracteres do padrão calculado.
- X é o valor do caracter na tabela ASCII
- R é a quantidade de caracteres do alfabeto utilizado, por exemplo R = 256 para o alfabeto ASCII estendido.  

O código abaixo calcula os valores de hash diminuindo a possibilidade de colisões entre padrão e texto, conforme a formula mostrada acima e considerando R = 256. 

    def stringSearchgHash(text, pattern):
        indexes = []

        pattern_value= 0
        r = 256**(len(pattern)-1)
        for character in pattern:
            pattern_value +=    (character) * r
            r/=256
        for i in range(len(text)):
            if (i+len(pattern)>len(text)):
                break
            j=i
            text_value = 0
            r = 256**(len(pattern))
            while(j<i+len(pattern)):
                text_value+=ord(text[j]) * r
                j+=1
                r/=256
            if (text_value==pattern_value):
                indexes.append(i)
        
        return indexes

## Usando o Hashing

Agora que _hash_ é algo além de uma palavra legal da computação, podemos seguir com o algoritimo desse encontro. O Rabin-Karp consiste em iterar com o hash value do padrão sobre o hash de cada parte do texto inteiro, como exemplificado na animação abaixo:

![simulacao1](simulacao1.gif)

Mas essa solução também tem um problema! É necessário acessar vários caracteres múltiplas vezes para pegar o seu valor. Como é possível observar na simulação acima, primeiro é calculado o valor de `ADA`, ou ,seja o valor de `A` + `D` + `A`, na proxima iteração, é calculado do valor de `DAC`, ou seja, `D` + `A` + `C` porém, o valor de `D` e `A` que já foi calculado na primeira iteração, é recalculado para a segunda. Fazendo o código dessa maneira ainda gera uma complexidade ruim de $$O(nm)$$ 

###
 

## Rabin-Karp 

O grande diferencial do algoritmo de Rabin-Karp que procura por um segmento de texto que tenha o mesmo _hash value_ do padrão, é o fato do mesmo utilizar o método de _rolling hash_, permitindo assim que ele tenha sua complexidade reduzida à $$O(n+m)$$ no melhor médio, tornando-o mais eficiente do que algoritimos triviais de complexidade $$O(nm)$$. 

Existem dois tipos de implementação desse algoritmo, o método de **Monte Carlo** e de **Las Vegas**. A primeira assume que não há nenhuma colisão durante a comparação. Quando o hash value do fragmento do texto bate com o do padrão, nenhuma comparação de caracteres é feita, por isso sua complexidade é $$O(n+m)$$ em todos os casos. Já a de _Las Vegas_ checa se os caracteres são realmente os mesmos, mas isso significa que em um caso em que todos os fragmentos de texto analisados têm o mesmo hash value do padrão, o código tem que realizar a comparação de caracteres _n_ vezes, tornando a complexidade em $$O(nm)$$ no seu pior caso.

As comparações de complexidade entre as implementações mencionadas podem ser vistas na tabela abaixo.  

![complexidade](complexidade.png)  


## Sobre o algoritmo
O Rabin-Karp pode ser utilizado como uma ferramenta de busca simples, porém onde ele tem seu valor destacado é dentro de sistemas de plágio, nos quais parágrafos de textos avaliativos ou científicos são colocados no programa como padrão de busca enquanto livros e banco de dados relacionados ao tema são colocados como texto aonde se quer encontrar alguma incidência de cópia indevida. 
Nesses casos, como a entrada é grande, o número de colisões se reduz significamente, pois o hash value fica cada vez mais específico e tendendo à ser único. O que garante que nesse tipo de aplicação o programa atue com seu melhor nivel de complexidade $$O(n+m)$$. 

## Overflow

Quando o padrão a ser calculado é muito grande, pode ocorrer problema de overflow. Para contornar isso, o algoritmo de Rabin-Karp utiliza _hashing modular_.  
Ou seja, toda vez que um valor de hash é calculado, é feito o modulo desse valor por Q ($$Value = Value % Q 0$$), onde Q é um inteiro maior que R (quantidade de caracteres do alfabeto utilizado). Para evitar colisões é interessante que o valor Q seja um número primo.
Abaixo temos o exemplo de um fórmula para cálcular um hash value utilizando modulação e técnicas para diminuir a possibilidade de colisões.


$$Value = ((R . X_{i-1}$$ % $$Q + t_{i-1}(Q-R^{M-1} $$%$$Q)).R + t_{1+M-1} A Q )$$


__________________________________________________
falar de rolling hash antes da versao com potencia e colisao para deixar claro que a ideia é mais eficiente

mostar o rolling hash com uma soma simples (subtrai que sai e soma o outro)

ORDEM
- o problema da versão de força bruta é comparar caracter por caracter para cada versão da janela
- aplicar a ideia de hashing vai comparar um valorzinho com outro valor
- atividade "so que tem um probleminha em termo de eficiencia" pra fazer as pessoas perceberem isso por conta propria
- rolling hash com soma simples e ter ganho de eficiencia
- mas tem a questao da colisao
- "os codigos estao horriveis, foi o leronardo que fez" hashimoto

Na parte das duas versoes colocar mais atividades e menos texto
Falar que o algoritimo pode dar a resposta errada. plano B compara coisa por coisa

possível ordem:
- falar da versao monte carlo que supoe que nao tem nenhuma colisao
- perguntar a complexidade no pior caso
- vamos supor que a gente queira um algoritimo que nao erre, isso significa que precisamos reverter por forca bruta? (ou alguma pergunta do tipo pra perceber que existe o plano B)

dar mais dicas de como chegar nas complexidades

e talvez deixar a tabela mais interativa pro aluno preencher alguma parte