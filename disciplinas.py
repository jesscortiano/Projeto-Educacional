###############################################################################
#   Jéssica Fernandes Cortiano
#   ADS
################################################################################
#   Módulo com operações das disciplinas
################################################################################


from utilidades import recuperar_arq, salvar_arq, buscar_item_por_codigo, ler_codigo_unico, ler_item_por_codigo

FILENAME = "info_disciplinas"

def ler_dados(disciplina):
    disciplina['nome'] = input("Nome Disciplina:")
    return disciplina


def inserir():
    dados_recuperados = recuperar_arq(FILENAME)

    codigo = ler_codigo_unico(dados_recuperados)

    disciplina = ler_dados({'codigo': codigo})

    dados_recuperados.append(disciplina)
    salvar_arq(FILENAME, dados_recuperados)



def editar():
    dados_recuperados = recuperar_arq(FILENAME)

    print("Digite o código da disciplina para editar")
    disciplina = ler_item_por_codigo(dados_recuperados)
    dados_recuperados.remove(disciplina)

    print("Digite os novos dados:")
    disciplina['codigo'] = ler_codigo_unico(dados_recuperados)

    disciplina = ler_dados(disciplina)

    dados_recuperados.append(disciplina)
    salvar_arq(FILENAME, dados_recuperados)

    print("Disciplina atualizado com sucesso!")
    input("Pressione ENTER para continuar")


def listar():
    dados_recuperados = recuperar_arq(FILENAME)
    for disciplina in dados_recuperados:
        print("-", disciplina)
    if len(dados_recuperados)==0:
        print("Não há disciplinas cadastrados")
    input("Pressione ENTER para continuar")


def excluir():
    dados_recuperados = recuperar_arq(FILENAME)
    print("Digite o código da disciplina para excluir")
    disciplina = ler_item_por_codigo(dados_recuperados)
    dados_recuperados.remove(disciplina)
    salvar_arq(FILENAME, dados_recuperados)

    print("Disciplina excluída com sucesso!")
    input("Pressione ENTER para continuar")
