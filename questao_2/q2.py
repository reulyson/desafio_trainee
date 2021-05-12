# Qual o ranking de estados por média de PIB per capita no ano de 2010?
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
    ranking = sorted(estado.items(), key=itemgetter(1), reverse=True) #utilizando sorted para ordenar em ordem, usando itemgetter eu chamo o valor na posição para ser ordenada.
    for i, v in enumerate(ranking):
        print(f'{i+1}° - {v[0]}')
ranking()


