cap = {
    '2010': 27832.52,
    '2011': 30303.38,
    '2012': 29837.10,
    '2013': 32201.90,
    '2014': 33370.72,
    '2015': 32597.83,
    '2016': 33534.48,
    '2017': 34373.88,
    '2018': 36445.75
}
def media():
    print('Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o dataset?')
    print('Informações:\n'
          'Ano 2010: R${:.2f}\n'
          'Ano 2011: R${:.2f}\n'
          'Ano 2012: R${:.2f}\n'
          'Ano 2013: R${:.2f}\n'
          'Ano 2014: R${:.2f}\n'
          'Ano 2015: R${:.2f}\n'
          'Ano 2016: R${:.2f}\n'
          'Ano 2017: R${:.2f}\n'
          'Ano 2018: R${:.2f}'.format(cap['2010'], cap['2011'], cap['2012'], cap['2013'],
                                      cap['2014'], cap['2015'], cap['2016'], cap['2017'], cap['2018']))

    media = (cap['2010']+cap['2011']+cap['2012']+cap['2013']+cap['2014']+cap['2015']+cap['2016']+cap['2017']+cap['2018']) / 9
    print('A média do PIB per capita de Manaus nos anos de 2010 à 2018 é R${:.2f}'.format(media))

nome = 'saida_q1.txt'
f = open('C:/Users/Reulyson Wanzeler/PycharmProjects/desafio_trainee_pib/questao_1/'+ nome, 'wt')
f.write(f'A média do PIB per capita de Manaus nos anos de 2010 à 2018 é R${media}')
f.close()

