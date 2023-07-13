################################################################################
#   Jéssica Fernandes Cortiano
#   ADS
################################################################################
#   Módulo com operações de turmas
################################################################################

from utilidades import recuperar_arq, salvar_arq, buscar_item_por_codigo, ler_codigo_unico, ler_item_por_codigo

import professores
import disciplinas

FILENAME = "info_turmas"


def ler_dados(turma):

    # Ler professor
    lista_professores = recuperar_arq(professores.FILENAME)
    print("Digite o código do professor")
    professor = ler_item_por_codigo(lista_professores)
    turma['codigo_professor'] = professor['codigo']

    # Ler disciplina
    lista_disciplinas = recuperar_arq(disciplinas.FILENAME)
    print("Digite o código da disciplina")
    disciplina = ler_item_por_codigo(lista_disciplinas)
    turma['codigo_disciplina'] = disciplina['codigo']

    return turma


def inserir():
    lista_turmas = recuperar_arq(FILENAME)

    nova_turma = {}

    codigo = ler_codigo_unico(lista_turmas)
    nova_turma['codigo'] = codigo
    nova_turma = ler_dados(nova_turma)

    lista_turmas.append(nova_turma)
    salvar_arq(FILENAME, lista_turmas)


def editar():
    lista_turmas = recuperar_arq(FILENAME)
    print("Digite o código para editar a turma")
    turma = ler_item_por_codigo(lista_turmas)
    lista_turmas.remove(turma)

    print("Digite os novos dados:")
    turma['codigo'] = ler_codigo_unico(lista_turmas)

    turma = ler_dados(turma)

    lista_turmas.append(turma)
    salvar_arq(FILENAME, lista_turmas)

    print("Turma atualizada com sucesso!")
    input("Pressione ENTER para continuar")
    

def listar():
    lista_turmas = recuperar_arq(FILENAME)
    for turma in lista_turmas:
        print("-", turma)
    if len(lista_turmas) == 0:
        print("Não há turmas cadastradas")
    input("Pressione ENTER para continuar")

def excluir():
    lista_turmas = recuperar_arq(FILENAME)
    print("Digite o código da turma para excluir seus dados")
    turma = ler_item_por_codigo(lista_turmas)
    lista_turmas.remove(turma)
    salvar_arq(FILENAME, lista_turmas)

    print("Turma excluída com sucesso!")
    input("Pressione ENTER para continuar")
    
    
    
    

