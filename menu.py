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




