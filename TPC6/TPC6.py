def criarturma():
    print("Turma criada com sucesso.")
    turma=[]
    return turma

def inseriralunonaturma(turma):
    nome=input("Introduza o nome do aluno")
    id=int(input("Introduza o id do aluno "))
    for a in turma:
        while id in a:
            print("Já existe um aluno com esse id.")
            id=int(input("Introduza o id do aluno. "))
    notaTPC=float(input("Introduza a nota do TPC. "))
    while notaTPC<0 or notaTPC>20:
        print("Nota inválida! (Nota deve estar entre 0 e 20 valores)")
        notaTPC=float(input("Introduza a nota do TPC"))
    notaProj=float(input("Introduza a nota do projeto"))
    while notaProj<0 or notaProj>20:
        print("Nota inválida! (Nota deve estar entre 0 e 20 valores)")
        notaProj=float(input("Introduza a nota do projeto"))
    notaTeste=float(input("Introduza a nota do teste"))
    while notaTeste<0 or notaTeste>20:
        print("Nota inválida! (Nota deve estar entre 0 e 20 valores)")
        notaTeste=float(input("Introduza a nota do teste:"))
    aluno=(nome,id,[notaTPC, notaProj, notaTeste])
    turma.append(aluno)

def listarTurma(turma):
    print("Listagem dos alunos da turma:")
    for a  in turma:
        print(a)

def consultarAluno(turma):
    id=int(input("Introduza o id do aluno que deseja consultar."))
    e=False
    for a in turma:
        if a[1]==id:
            print(a)
            e=True
    if e==False:
        print(f"O aluno com o id {id} não se encontra na turma.")


def linha(aluno):
    nome, id, notas = aluno
    return f"{nome},{id},{notas[0]},{notas[1]},{notas[2]}\n"

def guardarTurma(turma, fnome):
    file = open(fnome, "w")  
    for aluno in turma:        
        file.write(linha(aluno))  
    file.close()               
   
        
def carregar_turma():
    nome_arquivo = input("Nome do arquivo para carregar a turma (ex: turma.txt): ")
    global turma
    try:
        with open(nome_arquivo, 'r') as file:
            turma = []
            for linha in file:
                dados = linha.strip().split(',')
                if len(dados) == 5:
                    nome, id, notaTPC, notaProj, notaTeste = dados
                    aluno = (nome, id, [float(notaTPC), float(notaProj), float(notaTeste)])
                    turma.append(aluno)
        print(f"Turma carregada do arquivo {nome_arquivo}.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("Erro ao processar o arquivo. Verifique o formato dos dados.")



def menu():
    print("""
    1. Criar Turma
    2. Inserir aluno
    3. Listar turma
    4. Consultar aluno por id
    5. Guardar turma
    6. Carregar uma turma de um ficheiro
    0. Sair da aplicação
          """)

    opcao=int(input("Qual opção deseja selecionar?"))
    return opcao

op=menu()
while op!=0:
    if op ==1:
        turma=criarturma()
    elif op== 2:
        inseriralunonaturma(turma)
        print("Aluno inserido com sucesso.")
        res=input("Deseja continuar com esta operação?(sim ou não)")
        if res=="sim":
            inseriralunonaturma(turma)
    elif op==3:
        if not turma:
           print("Ainda não existem turmas.")
        else:
            listarTurma(turma)
    elif op==4:
        if not turma:
            print("Ainda não existem turmas.")
        else:
            consultarAluno(turma)
        res=input("Deseja continuar com esta operação?(sim ou não)")
        if res=="sim":
            consultarAluno(turma)
    elif op==5:
        if not turma:
           print("Ainda não existem turmas.")
        else:
            guardarTurma(turma, "turma.txt")
            print("Turma guardada  com sucesso.")
    elif op==6:
        if not turma:
           print("Ainda não existem turmas.")
        else:
            carregar_turma()

    op=menu()
print("Obrigado pela preferência!")  

