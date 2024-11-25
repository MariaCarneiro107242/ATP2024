cinema=[]
def criarsala(cinema):
    lugares=int(input("Quantos lugares tem a sala?"))
    bilhetesvendidos=0
    filme=input("Qual é o filme em exibição na sala?")
    sala=[lugares,bilhetesvendidos, filme]
    cinema.append(sala)


def removersalas(cinema):
    index = int(input("Introduza o índice da sala"))
    cinema.pop(index)
    print("A sala foi removida")
    print("Atualização de salas:", cinema)
    menu()


def listarsalas(cinema):
    for s in cinema:
        print(s)


def lugaresDisponíveis(cinema, filme):
    for s  in cinema:
        if s[2]==filme:
            ld=s[0]-s[1]
            return ld
    return False

   
def vendebilhete(cinema, filme, nbilhetes):
        for s in cinema:
            if s[2]==filme:
                s[1]=s[1]+nbilhetes
                print(f"Bilhetes vendidos com sucesso.\n Lugares Disponíveis:{lugaresDisponíveis(cinema,filme)}.")
        

def menu():
    print("""
    1. Criar sala
    2. Remover Sala
    3. Listar Salas
    4. Lugares Disponíveis
    5. Vender bilhetes
    0. Sair""")
    opcao=int(input("Qual opção deseja selecionar?"))
    return opcao


op=menu()
while op!=0:
    if op==1:
        criarsala(cinema)
    elif op==2:
        if not cinema:
            print("Cinema sem disponibilidade")
        else:
            removersalas(cinema)
    elif op==3:
        if not cinema:
            print("Cinema sem disponibilidade")
        else:
            listarsalas(cinema)
    elif op==4:
        if not cinema:
            print("Cinema sem disponibilidade")
        else:
            filme=input("Introduza o nome do filme: ")
            filme=filme.capitalize()
            ld=lugaresDisponíveis(cinema, filme)
            if ld== False:
                print("O filme não existe no cinema.")
            else:
                print(f"Existem {ld} lugares disponíveis no filme \"{filme}\". ")
    elif op == 5:
            filme = input("Introduza o nome do filme: ")
            filme=filme.capitalize()
            ld=lugaresDisponíveis(cinema, filme)
            if ld==False:
                print(f'O filme {filme} não existe no cinema.')
            else:
                nbilhetes = int(input('Quantos bilhetes pertende?'))
                if ld>=nbilhetes:
                    vendebilhete(cinema, filme, nbilhetes)
                else:
                    print('Para o número de bilhetes pretendidos não há lugares suficientes na sala.')
    else:
        print("Opção inválida.")

    op=menu()
print('Obrigada pela preferência.Aguardamos nova visita.')