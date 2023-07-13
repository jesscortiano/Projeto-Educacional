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

