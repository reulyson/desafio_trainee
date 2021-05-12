from questao_1 import q1
from questao_2 import q2
from questao_3 import q3
def menu():
    print('\nEscolha a baixo qual questão você deseja!\n'
          '\33[32m1 - Questão 1\33[m\n'
          '\33[32m2 - Questão 2\33[m\n'
          '\33[32m3 - Questão 3\33[m\n'
          '\33[32m0 - Encerrar questões\33[m'.center(137))

print('\33[34mDesafio Trainee Bemol\33[m')
menu()
while True:
    opcao = input('Qual sua opção? ')
    print('')
    if opcao == '1':
        q1.media()
        menu()
    elif opcao == '2':
        q2.ranking()
        print('\nProxima questão\n')
        menu()

    elif opcao == '3':
        print('Atividade')
        print('\nProxima questão\n')
        menu()
    elif opcao == '0':
        print('Fim das questões. Obrigado!')
        break
    else:
        print('\33[31mOpção invalida\33[m')
        menu()

