#3. Qual a proporção do valor adicionado bruto médio do setor de serviços(8) em relação ao valor adicionado bruto total médio no estado do Amazonas no ano de 2018?

#armazenamento do dataset em uma lista e semparando sempre que encontrar um ';'
arquivo = open('dataset/pib_municipio_2010_a_2018.txt', 'r', encoding='utf-8')
conteudo = arquivo.readlines()
conteudo_list = [x.split(";") for x in conteudo]
arquivo.close()

def proporcao():

    lista_servico = []
    lista_total = []

#Somando PIB de cada estado
    for linha in conteudo_list[1:]:
        if linha[0] == '2018' and linha[2] == 'Amazonas':
            lista_servico.append(float(linha[8]))
            lista_total.append(float(linha[10]))

    media_servico = sum(lista_servico) / len(lista_servico)
    media_total = sum(lista_total) / len(lista_total)

    resultado_valores = (media_servico/media_total)
    resultado_porcentagem = "{:.2f}%".format(media_servico/media_total*100)

    print("A proporção do setor de serviços pelo total em valores é: ", resultado_valores)
    print("A proporção do setor de serviços pelo total em porcentagem é: ", resultado_porcentagem)

    with open('questao_03/saida_q3.txt', 'w') as file:
        file.write(f"A proporção do setor de serviços pelo total em valores é:{resultado_valores}\n A proporção do setor de serviços pelo total em porcentagem é:{resultado_porcentagem}")
    file.close()