###############################################################################
#   Jéssica Fernandes Cortiano
#   ADS
################################################################################
#   Módulo com operações dos Professores
################################################################################


from utilidades import recuperar_arq, salvar_arq, buscar_item_por_codigo, ler_codigo_unico, ler_item_por_codigo

FILENAME = "info_professores"

def ler_dados(professor):
    professor['nome'] = input("Nome Professor:")
    professor['cpf'] = input("CPF Professor:")
    return professor


def inserir():
    dados_recuperados = recuperar_arq(FILENAME)

    codigo = ler_codigo_unico(dados_recuperados)

    professor = ler_dados({'codigo': codigo})

    dados_recuperados.append(professor)
    salvar_arq(FILENAME, dados_recuperados)



def editar():
    dados_recuperados = recuperar_arq(FILENAME)

    print("Digite o código do professor para editar")
    professor = ler_item_por_codigo(dados_recuperados)
    dados_recuperados.remove(professor)

    print("Digite os novos dados:")
    professor['codigo'] = ler_codigo_unico(dados_recuperados)

    professor = ler_dados(professor)

    dados_recuperados.append(professor)
    salvar_arq(FILENAME, dados_recuperados)

    print("Professor atualizado com sucesso!")
    input("Pressione ENTER para continuar")


def listar():
    dados_recuperados = recuperar_arq(FILENAME)
    for professor in dados_recuperados:
        print("-", professor)
    if len(dados_recuperados)==0:
        print("Não há Professores cadastrados")
    input("Pressione ENTER para continuar")


def excluir():
    dados_recuperados = recuperar_arq(FILENAME)
    print("Digite o código do professor para excluir")
    professor = ler_item_por_codigo(dados_recuperados)
    dados_recuperados.remove(professor)
    salvar_arq(FILENAME, dados_recuperados)

    print("Professor excluído com sucesso!")
    input("Pressione ENTER para continuar")
