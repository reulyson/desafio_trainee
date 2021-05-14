<h1 align="center">Desafio Trainee Bemol</h1>

<p align="center">
  <a href="#dart-sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#white_check_mark-q1">Q1</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-q2">Q2</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-q3">Q3</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-menu">Menu</a> &#xa0; | &#xa0;
  <a href="https://github.com/reulyson" target="_blank">Autor</a>
</p>

<br>

## :dart: Sobre ##

A seguir as questões a serem respondidas a partir do dataset fornecido:

1. Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o dataset?
2. Qual o ranking de estados por média de PIB per capita no ano de 2010? 
3. Qual a proporção do valor adicionado bruto médio do setor de serviços em relação ao valor adicionado bruto total médio no estado do Amazonas no ano de 2018?

###### Seguindo as observações de não poder usar bibliotecas numpy, pandas e etc.
###### Foi utilizado a versão do Python 3.9.5.
###### O script foi desenvolvido usando o SO Windows 10.

## :white_check_mark: Q1 ##

Na primeira questão, meu maior desafio foi filtrar os dados necessários para resolver o problema. De primeira eu fiz a coleta de dados de forma direta no arquivo txt e utilizei esse código:

```python
per_capita = {'2010':27832.52,
'2011': 30303.38, 
'2012': 29837.10,
'2013': 32201.90,
'2014': 33370.72,
'2015': 32597.83,
'2016': 33534.48,
'2017': 34373.88,
'2018': 36445.75}
media=(per_capita['2010']+per_capita['2011']+per_capita['2012']+per_capita['2013']+per_capita['2014']+per_capita['2015']+per_capita['2016']+
per_capita['2017']+per_capita['2018'])/(len(per_capita))
print('A média per capita de manaus entre 2010 a 2018 foi {:.2f}'.format(media))
```

Porém após pesquisar um pouco mais e revisar os vídeos do curso criei um script que percorre o arquivo do dataset para que pudesse filtrar os dados necessários. Desta maneira resolver o problema em si foi bem mais simples, criando uma lista para armazenar todos os valores per captos de cada ano de Manaus salvando a variável 'lib', depois somando cada um desses valores e dividindo pela quantidade de anos pedidos para assim chegar ao resultado esperado.

:heavy_check_mark: q1 respondida;

## :white_check_mark: Q2 ##

Antes de criar o script que seria realmente utilizado, eu criei um outro anteriormente a esse, para entender a mecânica que eu deveria usar para criar o ranking, para esse teste eu usei o seguinte script: No teste importei duas bibliotecas do próprio python, random(randint) uma permitia que o computador gerasse números aleatórios e o operator(itemgetter) me permitia chamar valores, usando o comando sorted era possível ordenar esse dicionário, porém os números eram ordenados do menor para o maior, então usei reverse= para inverter os valores ordenados.

```python
from random import randint
from operator import itemgetter
estado = {'am': randint(0, 6),
          'pa': randint(0, 6),
          'sp': randint(0, 6),
          'rj': randint(0, 6)}
ranking = dict()
def ranking():
    for e, m in estado.items():
        print(f'O estado {e} tem uma media de {m}')
    ranking = sorted(estado.items(), key=itemgetter(1), reverse=True)
    for i, v in enumerate(ranking):
        print(f'{i+1}° - {v[0]}')
ranking()
```

Para a resolução eu utilizei a mesma premissa da questão 1 para a média dos estados, e me basei no script acima para gerar o ranking, porém, troquei a função itemgetter da biblioteca operator por lambda, que está também chamando o valor, porém o desafio pede que não se use bibliotecas na resolução do desafio (por mais que as bibliotecas padrões do python tivessem sido permitidas, optei por não utilizar). No final o resultado foi impresso de forma correta. Porém nessa questão me deparei que nas saídas dos arquivos txt da questão, os nomes dos estados que possuíam acentos não estavam aparecendo, pesquisando um pouco encontrei que o SO Windows não imprime em arquivos strings com acentos, pois a representação de uma string como uma lista de pontos de código é abstrata então para decodificá-la usei então encoding='utf-8' resolvendo o problema.

:heavy_check_mark: q2 respondida;

## :white_check_mark: Q3 ##

Para resolver esta questão precisei utilizar a mesma dinâmica utilizada na primeira, o que me fez analisar que a primeira questão foi realmente a base para a resolução de todas as outras questões, pois todas pediram média de valores diferenciando alguns detalhes, o detalhe da questão três era mais em questão de pesquisa, precisei procurar por resoluções de proporção e criar uma lógica que pudesse funcionar no script. Então criei duas listas para armazenar os valores o valor de serviços e outra para armazenar o valor bruto total, logo depois criei as médias necessárias para a resolução final, que foi a proporção que era equivalente a média dos serviços dividido pela média total, e me dei liberdade para criar uma porcentagem que mostrasse essa proporção.

:heavy_check_mark: q3 respondida;

## :white_check_mark: Menu ##

De início importei cada uma das questões, e defini uma função nomeada menu para ser chamada nos blocos de cada questão, os scripts das questões também foram definidos como função. Depois criei um loop que me permitia percorrer opções para cada questão e uma para encerrar o programa, para cada bloco  da questão fiz a chamada da função referente à questão escolhida e logo após a função menu para permitir seguir o loop, repetir isso para todas as outras alternativas, também determinei 0 como o comando para encerrar o programa. Por fim, criei um bloco para caso o usuário digitasse o numero errado ou alguma outra informação diferente do definido. E assim encerrei o menu desse programa.

:heavy_check_mark: main finalizado;

<a href="#top">Voltar para o topo</a>
