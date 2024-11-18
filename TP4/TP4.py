
1import random
tecla = (-1)
lista = []


while tecla != 0:
    print('''Bem-vindo! O menu que temos para si:
    (1) Criar Lista
    (2) Ler Lista
    (3) Soma de todos os valores da lista
    (4) Média dos valores
    (5) Maior
    (6) Menor
    (7) Confirmar ordenação por ordem crescente
    (8) Confirmar ordenação por ordem decrescente
    (9) Procura um elemento
    (0) Sair''')
   
    tecla = int(input('Introduza o número corresponde à operação que pretende efetuar: '))

    if tecla == 1:
        tamanho = int(input('Quantos elementos pretende que a sua lista tenha?'))
        lista = [random.randrange(1,101) for x in range (tamanho)]
        print(lista)
        input('Voltar ao menu')


    elif tecla == 2:
        tamanho = int(input('Quantos elementos pretende que a sua lista tenha?'))
        i = 0
        lista = []
        while tamanho > 0:
            i = i + 1
            num = int(input(f'Introduza o {i}º número da sua lista:'))
            lista.append(num)
            tamanho = tamanho - 1
        print(lista)
        input('Voltar ao menu')

    if tecla == 3:
        if lista == []:
            print('''É necessário criar uma lista.
                  No menu seleciona 1 ou 2.''')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            soma = 0
            while i < tamanho:
                num = lista[i]
                i = i + 1
                soma = soma + num
            print(f'A soma é {soma}.')
        input('Voltar ao menu:')
        
    elif tecla == 4:
        if lista == []:
            print('''É necessário criar uma lista.
                  No menu seleciona 1 ou 2.''')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            soma = 0
            while i < tamanho:
                num = lista[i]
                i = i + 1
                soma = soma + num
            media = soma / i
            print(f'A média é {media}.')
        input('Voltar ao menu')

    elif tecla == 5:
        if lista == []:
            print('''É necessário criar uma lista.
                  No menu seleciona 1 ou 2.''')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            maior = 0
            while i < tamanho:
                num = lista[i]
                i = i + 1
                if num > maior:
                    maior = num
            print(f'O maior número é {maior}')
        input('Voltar ao menu')

    elif tecla == 6:
        if lista == []:
            print('''É necessário criar uma lista.
                  No menu seleciona 1 ou 2.''')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            menor = num
            while i < tamanho:
                num = lista[i]
                i = i + 1
                if num < menor:
                    menor = num
            print(f'O menor número é {menor}')
        input('Voltar ao menu')

    elif tecla == 7:
        if lista == []:
            print('''É necessário criar uma lista.
                  No menu seleciona 1 ou 2.''')
        else:
            print(lista)
            tamanho = len(lista) - 1
            i = 0
            while i < tamanho :
                if lista[i] < lista [i + 1] :
                    i = i + 1
                    if i == tamanho :
                        print('Confirma-se.')
                else :
                    print('Negativo.')
                    i = tamanho
        input('Voltar ao menu')

    elif tecla == 8:
        if lista == []:
            print('''É necessário criar uma lista.
                  No menu seleciona 1 ou 2.''')
        else:
            print(lista)
            tamanho = len(lista) - 1
            i = 0
            while i < tamanho :
                if lista[i] > lista [i + 1] :
                    i = i + 1
                    if i == tamanho :
                        print('Confrirma-se.')
                else :
                    print('Negativo.')
                    i = tamanho
        input('Voltar ao menu')


    elif tecla == 9 :
        if lista == []:
            print('''É necessário criar uma lista.
                  No menu seleciona 1 ou 2.''')
        else:
            print(lista)
            tamanho = len(lista)
            i = 0
            elem = int(input('Introduza o elemento que pretende procurar na lista: '))
            if elem in lista :
                while i < tamanho:
                    if lista[i] == elem:
                        print(f'A sua posição é {i + 1}')
                        i = tamanho
                    else:
                        i = i + 1
            else:
                print('A sua posição é -1')
        input('Voltar ao menu')


    elif tecla < 0 or tecla > 9:
        tecla = input('Opção inválida, carrega para voltares ao menu: ')


print('Até Breve!')
print(lista)