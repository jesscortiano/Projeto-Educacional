################################################################################
#   Jéssica Fernandes Cortiano
#   ADS
################################################################################
#   Módulo com operações de estudante
################################################################################


from utilidades import recuperar_arq, salvar_arq, buscar_item_por_codigo, ler_codigo_unico, ler_item_por_codigo

FILENAME = "info_estudantes"


def ler_dados(estudante):
    estudante['nome'] = input("Nome Estudante:")
    estudante['cpf'] = input("CPF Estudante:")
    return estudante


def inserir():
    dados_recuperados = recuperar_arq(FILENAME)

    codigo = ler_codigo_unico(dados_recuperados)

    estudante = ler_dados({'codigo': codigo})

    dados_recuperados.append(estudante)
    salvar_arq(FILENAME, dados_recuperados)



def editar():
    dados_recuperados = recuperar_arq(FILENAME)

    print("Digite o código do estudante para editar seus dados")
    estudante = ler_item_por_codigo(dados_recuperados)
    dados_recuperados.remove(estudante)

    print("Digite os novos dados:")
    estudante['codigo'] = ler_codigo_unico(dados_recuperados)

    estudante = ler_dados(estudante)

    dados_recuperados.append(estudante)
    salvar_arq(FILENAME, dados_recuperados)

    print("Estudante atualizado com sucesso!")
    input("Pressione ENTER para continuar")


def listar():
    dados_recuperados = recuperar_arq(FILENAME)
    for estudante in dados_recuperados:
        print("-", estudante)
    if len(dados_recuperados)==0:
        print("Não há estudantes cadastrados")
    input("Pressione ENTER para continuar")


def excluir():
    dados_recuperados = recuperar_arq(FILENAME)
    print("Digite o código do estudante para excluir seus dados")
    estudante = ler_item_por_codigo(dados_recuperados)
    dados_recuperados.remove(estudante)
    salvar_arq(FILENAME, dados_recuperados)

    print("Estudante excluído com sucesso!")
    input("Pressione ENTER para continuar")
