################################################################################
#   Jéssica Fernandes Cortiano
#   ADS
################################################################################
#   Módulo com operações de matriculas
################################################################################

from utilidades import recuperar_arq, salvar_arq, buscar_item_por_codigo, ler_codigo_unico, ler_item_por_codigo

import turmas
import estudantes

FILENAME = "info_matriculas"


def procurar_matricula_duplicada(lista_matriculas, turma, estudante):
    for matricula in lista_matriculas:
        if (matricula['codigo_estudante'] == estudante['codigo']) and (matricula['codigo_turma'] == turma['codigo']):
            return matricula
    # Acabou a lista e nao achei nada
    return None


def ler_dados(matricula):
    lista_matriculas = recuperar_arq(FILENAME)
    lista_turmas = recuperar_arq(turmas.FILENAME)
    lista_estudantes = recuperar_arq(estudantes.FILENAME)

    while True:
        # Ler turma
        print("Digite o código da turma")
        turma = ler_item_por_codigo(lista_turmas)

        # Ler estudante
        print("Digite o código do estudante")
        estudante = ler_item_por_codigo(lista_estudantes)

        # Procurar duplicado
        duplicado = procurar_matricula_duplicada(lista_matriculas, turma, estudante)
        if duplicado is None:
            # Ok, matricula nao existe
            break
        else:
            # Ops, matricula ja existe
            continue

    matricula['codigo_turma'] = turma['codigo']
    matricula['codigo_estudante'] = estudante['codigo']

    return matricula


def inserir():
    lista_matriculas = recuperar_arq(FILENAME)

    nova_matricula = {}
    nova_matricula = ler_dados(nova_matricula)

    lista_matriculas.append(nova_matricula)
    salvar_arq(FILENAME, lista_matriculas)


def listar():
    lista_matriculas = recuperar_arq(FILENAME)
    for matricula in lista_matriculas:
        print("-", matricula)
    if len(lista_matriculas) == 0:
        print("Não há matrículas cadastradas")
    input("Pressione ENTER para continuar")


def excluir():
    lista_matriculas = recuperar_arq(FILENAME)
    lista_turmas = recuperar_arq(turmas.FILENAME)
    lista_estudantes = recuperar_arq(estudantes.FILENAME)

    while True:
        print("Digite os dados da matrícula para excluir")

        print("Digite o código da turma:")
        turma = ler_item_por_codigo(lista_turmas)

        print("Digite o código do estudante:")
        estudante = ler_item_por_codigo(lista_estudantes)

        matricula = procurar_matricula_duplicada(lista_matriculas, turma, estudante)
        if matricula is None:
            print('Dados não enontrados, digite novamente ...')
            continue
        else:
            lista_matriculas.remove(matricula)
            salvar_arq(FILENAME, lista_matriculas)
            break

    print("Matrícula excluída com sucesso!")
    input("Pressione ENTER para continuar")


def editar():
    lista_matriculas = recuperar_arq(FILENAME)
    lista_turmas = recuperar_arq(turmas.FILENAME)
    lista_estudantes = recuperar_arq(estudantes.FILENAME)

    while True:
        print("Digite os dados da matrícula para editar")

        print("Digite o código da turma:")
        turma = ler_item_por_codigo(lista_turmas)

        print("Digite o código do estudante:")
        estudante = ler_item_por_codigo(lista_estudantes)

        matricula = procurar_matricula_duplicada(lista_matriculas, turma, estudante)
        if matricula is None:
            print('Dados não enontrados, digite novamente ...')
            continue
        else:
            lista_matriculas.remove(matricula)

            print("Digite os novos dados:")
            ler_dados(matricula)

            lista_matriculas.append(matricula)
            salvar_arq(FILENAME, lista_matriculas)
            break

    print("Matrícula editada com sucesso!")
    input("Pressione ENTER para continuar")
