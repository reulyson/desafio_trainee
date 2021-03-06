#Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o dataset?

#armazenamento do dataset em uma lista e semparando sempre que encontrar um ';'
arquivo = open('dataset/pib_municipio_2010_a_2018.txt', 'r', encoding='utf-8')
conteudo = arquivo.readlines()
conteudo_list = [x.split(";") for x in conteudo]
arquivo.close()

#criando função para chamar no main
def media():
#criando uma lista com todo o contudo, se linha [3] - referente a municipio - for manaus.
#e esta adcionando a lista todos o conteudo da ultima linha referente a per capita, e tratando quebras de linhas e espaços vazios
    pib = []
    for linha in conteudo_list[1:]:
        if linha[3] == 'Manaus':
            pib.append(float(linha[-1].replace('\n', '')))

#calculando da media percapita
    media = sum(pib)/len(pib)

#imprimido o calculo da média percapita
    print("1. Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o dataset?\n")
    print("Média percapita de Manaus: R${:.2f}".format(media))

#criando arquivo de saida_q1 e escrevendo conteudo
    with open('questao_01/saida_q1.txt', 'w', encoding="utf-8") as file:
        file.write("1.Qual o valor médio de PIB per capita da cidade de Manaus no período que abrange o dataset?\n")
        file.write("Média percapita de Manaus: R${:.2f}".format(media))
    file.close()
