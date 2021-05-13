#2. Qual o ranking de estados por média de PIB per capita no ano de 2010?

#armazenamento do dataset em uma lista e semparando sempre que encontrar um ';'
arquivo = open('dataset/pib_municipio_2010_a_2018.txt', 'r', encoding='utf-8')
conteudo = arquivo.readlines()
conteudo_list = [x.split(";") for x in conteudo]
arquivo.close()

def ranking():

# listar estados
    estados = []
    for linha in conteudo_list[1:]:
        estados.append(linha[2])
    estados = list(set(estados))

# criar dicionário
    dict_estados = {}
    for estado in estados:
        dict_estados[estado] = []

#Somando PIB de cada estado
    for linha in conteudo_list[1:]:
        if linha[0] == '2010':
            dict_estados[linha[2]].append(float(linha[-1].replace('\n', '')))

    for estado in estados:
# Transformando lista em médias
        dict_estados[estado] = sum(dict_estados[estado])/len(dict_estados[estado])
    
# reordenando dicionario pelo maior valor
    dict_estados = dict(sorted(dict_estados.items(), key=lambda item: item[1], reverse=True))

    for r in dict_estados:
        print(r)

    with open('questao_02/saida_q2.txt', 'w', encoding='utf-8') as file:
        file.write("Ranking de estados por média de PIB per capita no ano de 2010:\n{}".format(dict_estados))
    file.close()
