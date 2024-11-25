#menu 
def menu():
    print('Bem-vindo ao jogo dos 21 fósforos!')
    print('Cada jogador retira, à vez, no mínimo 1 e no máximo 4 fósforos. Quem retirar o último fósforo perde.')
    print('1.Quero ser o primeiro a jogar.')
    print('2.Quero ser o segundo a jogar.')
    print('3.Quero sair do jogo.')

#Utlizador é o primeiro a jogar 
def pri():
    fosf=21
    while fosf > 1:
        salto = int(input('Quantos fósforos retiras?'))
        while salto > 4 or salto < 1:  
            print ('Cada jogador retira, à vez, no mínimo 1 e no máximo 4 fósforos.')
            salto = int(input('Quantos fósforos retiras?'))
        fosf = fosf - salto
        comp = 5 - salto
        fosf = fosf - comp
        print (f'Eu retiro {comp} fósforos. Sobram {fosf}. Quantos retiras?')
    print ('Pesdeste porque ficaste com o último fósforo.')

#utilizador é o segundo a jogar
def seg():
    from random import randint
    fosf = 21
    while fosf > 1:
        comp = randint (1,4)
        fosf = fosf - comp 
        salto = int (input(f'Eu tirei {comp} fósforos. Sobram {fosf}. Quantos retiras?'))
        while salto > 4:
            print('Cada jogador retira, à vez, no mínimo 1 e no máximo 4 fósforos.')
            salto =  int(input('Quantos fósforos retiras?'))
        while salto < 1:
            print ('Cada jogador retira, à vez, no mínimo 1 e no máximo 4 fósforos.')
            salto = int(input('Quantos fósforos retiras?'))
        fosf= fosf - salto
        if fosf == 1:
            print ('Ganhaste! Parabéns!')
        if salto != 5 - comp:
            if fosf > 16:
                comp = fosf - 16
            elif fosf > 11:
                comp = fosf - 11
            elif fosf > 6:
                comp = fosf - 6
            elif fosf > 1:
                comp = fosf - 1

            fosf =  fosf - comp 
            while fosf > 1:
                salto = int(input(f'Eu retiro {comp} fósforos. Sobram {fosf}. Quantos retiras?'))
                while salto > 4:
                    print('Cada jogador retira, à vez, no mínimo 1 e no máximo 4 fósforos.')
                    salto = int(input('Quantos fósforos retiras?'))
                fosf = fosf - salto
                comp = 5 - salto
                fosf = fosf - comp
            print ('Perdeste porque ficaste com o último fósforo')


menu()
opcao = int(input('Selecione uma das opções.'))

while opcao != 3:
    if opcao == 1:
        pri()
    elif opcao == 2:
        seg()
    else:
        print('Opção inválida')
    menu()
    opcao= int(input('Selecione uma das opções.'))

print('Fim do jogo!Aguardamos o próximo encontro!')