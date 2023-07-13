################################################################################
#   Jéssica Fernandes Cortiano
#   ADS
################################################################################


import utilidades
import estudantes
import disciplinas
import professores
import turmas
import matriculas


################################################################################
#   Funções Menu
################################################################################

def exibir_menu_principal():
    print("--MENU PRINCIPAL--\n",
          "(1) Estudante \n",
          "(2) Disciplina \n",
          "(3) Professor \n",
          "(4) Turma \n",
          "(5) Matrícula \n",
          "(9) Sair \n")


def exibir_menu_operacao(placeholder):
    print(f"**[{placeholder}] MENU OPERAÇÕES**\n",
          "(1) Incluir\n",
          "(2) Listar\n",
          "(3) Atualizar\n",
          "(4) Excluir\n",
          "(9) Voltar ao Menu Principal\n")


def solicitar_opcao():
    opcao = int(input("escolha uma opção: "))
    return opcao


################################################################################
#   Operações
################################################################################

def incluir(nome_opcao):
    while True:
        if nome_opcao == 'ESTUDANTE':
            estudantes.inserir()
        elif nome_opcao == 'DISCIPLINA':
            disciplinas.inserir()
        elif nome_opcao == 'PROFESSOR':
            professores.inserir()
        elif nome_opcao == 'TURMA':
            turmas.inserir()
        elif nome_opcao == 'MATRÍCULA':
            matriculas.inserir()

        if input(f'Deseja incluir  {nome_opcao} (s/n): ') == "n":
            break


def listar(nome_opcao):
    if nome_opcao == 'ESTUDANTE':
        estudantes.listar()
    elif nome_opcao == 'DISCIPLINA':
        disciplinas.listar()
    elif nome_opcao == 'PROFESSOR':
        professores.listar()
    elif nome_opcao == 'TURMA':
        turmas.listar()
    elif nome_opcao == 'MATRÍCULA':
        matriculas.listar()


def editar(nome_opcao):
    if nome_opcao == 'ESTUDANTE':
        estudantes.editar()
    elif nome_opcao == 'DISCIPLINA':
        disciplinas.editar()
    elif nome_opcao == 'PROFESSOR':
        professores.editar()
    elif nome_opcao == 'TURMA':
        turmas.editar()
    elif nome_opcao == 'MATRÍCULA':
        matriculas.editar()


def excluir(nome_opcao):
    if nome_opcao == 'ESTUDANTE':
        estudantes.excluir()
    elif nome_opcao == 'DISCIPLINA':
        disciplinas.excluir()
    elif nome_opcao == 'PROFESSOR':
        professores.excluir()
    elif nome_opcao == 'TURMA':
        turmas.excluir()
    elif nome_opcao == 'MATRÍCULA':
        matriculas.excluir()


################################################################################
#   Código (Main)
################################################################################


opcao = 0
nome_opcao = ""

while opcao != 9:
    exibir_menu_principal()
    opcao = solicitar_opcao()

    if opcao == 1:
        nome_opcao = "ESTUDANTE"

    elif opcao == 2:
        nome_opcao = "DISCIPLINA"

    elif opcao == 3:
        nome_opcao = "PROFESSOR"

    elif opcao == 4:
        nome_opcao = "TURMA"

    elif opcao == 5:
        nome_opcao = "MATRÍCULA"

    elif opcao == 9:
        break
    else:
        print("Opção inválida")
        continue

################################################################################

    operacao = 0

    while operacao != 9:
        exibir_menu_operacao(nome_opcao)
        operacao = int(input("escolha uma opção:"))
        if operacao == 1:
            print("===INCLUSÃO===\n")

            incluir(nome_opcao)

        elif operacao == 2:
            print("===LISTAGEM===\n")

            listar(nome_opcao)

        elif operacao == 3:
            print("===ATUALIZAR===")

            editar(nome_opcao)

        elif operacao == 4:
            print("===EXCLUIR===")


            excluir(nome_opcao)

        elif operacao == 9:
            pass
        else:
            print ("Opção Inválida")

