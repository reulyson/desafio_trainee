# Desafio Treinee

A seguir as questões a serem respondidas a partir do dataset fornecido:
1. Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o
dataset?
2. Qual o ranking de estados por média de PIB per capita no ano de 2010? 
3. Qual a proporção do valor adicionado bruto médio do setor de serviços em relação ao valor
adicionado bruto total médio no estado do Amazonas no ano de 2018?

###### Seguindo as observações de não poder usar bibliotecas numpy, pandas e etc
###### Foi utilizando a versão do Python 3.9.5.
###### O script foi desenvlvido usando o SO Windows 10

## Resolução da primeira questão
A primeira questão meu maior desafio foi filtrar os dados necessarios para resolver o problema. De primeira eu fiz a coleta de dados de forma direta no arquivo txt e ultilizei esse código:
'''java script
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
''''
Porém após pesquisar um pouco mais e revisar os vídeos do curso criei um script que percorre o arquivo do dataset para que pudesse filtrar os dados necessários.
Desta maneira resolver o prblema em si foi bem mais simples, criando uma lista para armazenar todos os valores per capitos de cada ano de Manaus salvamdo a variavel 'lib', depois somando cada um desses valores e dividindo pela quantidade de anos pedidos para assim chegar ao resultado esperado. 
- [x] Primeira questão respondida

## Resolução da segunda questão
Antes de criar o script que seria realmente ultilizado, eu criei um antes para entender a mecânica que eu deveria usar para criar o ranking, para esse teste eu usei o seguinte script. No teste importei duas bibliotecas do proprio python, ramdon(randint) uma permitia que o computador gerasse nuemros aleatoris e operator(itemgetter) me permitia chamar valores, e usando o comando sorted era possivel ordenar esse dicionario, porém os numeros eram ordenados do menor para o maior, então usei reverse= para reverter os valores ordenados.
'''java scripit
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
    ranking = sorted(estado.items(), key=itemgetter(1), reverse=True) #utilizando sorted para ordenar, usando itemgetter eu chamo o valor na posição para ser ordenada.
    for i, v in enumerate(ranking):
        print(f'{i+1}° - {v[0]}')
ranking()
'''
Para a resolução eu utlizei a mesma premissa do da questão 1 para a média dos estados, e me basei no script a cima para gerar o ranking, porém torquei a função itemgetter da biblioteca operator por lambda, que está também chamando o valor, porém o desafio pede que não se use bibliotecas na resolução do desafio (por mais que as bibliotecas padrões do python tivessem sido permitidas, optei por não utilizar). No final o resultado foi imprimido de forma correta. Porem nssa questão me deparei que nas saidas dos arquivos txt da questao, os nomes dos estados que possuiam acentos não estavam aparecendo, pesquisando um pouco encotrei que o SO Windows não imprime em arquivos strings com acentos, pois a representação de uma string como uma lista de pontos de código é abstrata entao para decodifica-la usei então encoding='utf-8' resolvendo o problema.
- [x] Segunda questão respondida

## Resolução da terceira questão

- [x] Terceira questão respondida

## Criando um menu com main.py para gerir os scripts
blablablabla fiz isso e aquilo para poder chegar ao resultado
- [x] Menú criado   