################################################################################
#   Jéssica Fernandes Cortiano
#   ADS
################################################################################
#   Módulo com utilidades
################################################################################

import json


def buscar_item_por_codigo(lista, codigo):
    for item in lista:
        if item['codigo'] == codigo:
            return item
    return None


def ler_codigo_unico(lista):
    while True:
        codigo = int(input("Código: "))
        if buscar_item_por_codigo(lista, codigo) == None:
            return codigo
        print('Código digitado já existe na lista.')


def ler_item_por_codigo(lista):
    while True:
        codigo = int(input("Código: "))
        item = buscar_item_por_codigo(lista, codigo)

        if item == None:
            print('Código digitado não existe!')
            continue
        else:
            return item


def salvar_arq(filename, data):
    """
    Função que salva os dados em um arquivo JSON.
    :param filename: Nome do arquivo.
    :param data: Dados para salvar no arquivo.
    :return: Nada.
    """

    with open(filename + '.json', 'w') as f:
        json.dump(data, f)
        print(f'INFO: Arquivo "{filename}" foi salvo com sucesso!')


def recuperar_arq(filename):
    """
    Função que carrega os dados de um arquivo JSON.
    :param filename: Nome do arquivo.
    :return: Lista dos dados carregados. Se não existir arquivo, retornará lista vazia.
    """

    try:
        with open(filename + '.json', 'r') as f:
            dados = json.load(f)
            return dados
    except FileNotFoundError:
        print(f'WARNING: Arquivo "{filename}" não foi encontrado.')
        return []
