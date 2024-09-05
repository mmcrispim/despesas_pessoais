# main.py
import pandas as pd


# Função principal
def processar_csv(caminho_arquivo_entrada, caminho_arquivo_saida):

    print(f'Caminho {caminho_arquivo_entrada}')

    # Leitura do arquivo CSV
    df = pd.read_csv(caminho_arquivo_entrada, header=0, sep=';', decimal=',')

    # Contar o número de registros (linhas)
    numero_registros = len(df)

    # Verificar se o arquivo tem dados
    print()  # Linha em branco para separar a saída de cada coluna
    if numero_registros > 0:
        print(f'O arquivo contém {numero_registros} registros.')
    else:
        print('O arquivo está vazio.')

    # Exibindo as primeiras 5 linhas do DataFrame
    print()  # Linha em branco para separar a saída de cada coluna
    print(f'Amostra do arquivo {df.head()}')

    # Renomear colunas
    df.rename(
        columns={
            'DT COMPRA': 'DT_COMPRA',
            'RECEITA DESPESA': 'RECEITA_DESPESA',
            'FORMA PAGTO': 'FORMA_PAGTO',
            'VLR TOTAL': 'VLR_TOTAL',
            'QTD PARCELAS': 'QTD_PARCELAS',
            'NUM PARCELA': 'NUM_PARCELA',
        },
        inplace=True,
    )

    # Exibindo as primeiras 5 linhas do DataFrame
    print()  # Linha em branco para separar a saída de cada coluna
    print(f'Amostra do arquivo com colunas renomeadas{df.head()}')

    # Criando novas colunas
    df['VLR_PARCELA'] = (df['VLR_TOTAL'] / df['QTD_PARCELAS']).round(2)

    # Exibindo as primeiras 5 linhas do DataFrame
    print()  # Linha em branco para separar a saída de cada coluna
    print(f'Amostra do arquivo {df.head()}')

    # Criando DataFrames separados
    receita_despesa = (
        df[['RECEITA_DESPESA']].drop_duplicates().reset_index(drop=True)
    )
    forma_pagto = df[['FORMA_PAGTO']].drop_duplicates().reset_index(drop=True)
    tipo = df[['TIPO']].drop_duplicates().reset_index(drop=True)
    categoria = df[['CATEGORIA']].drop_duplicates().reset_index(drop=True)
    item = df[['ITEM']].drop_duplicates().reset_index(drop=True)
    status = df[['STATUS']].drop_duplicates().reset_index(drop=True)

    # Substituindo valores pelos índices
    for col in [
        'RECEITA_DESPESA',
        'FORMA_PAGTO',
        'TIPO',
        'CATEGORIA',
        'ITEM',
        'STATUS',
    ]:
        df[col] = df[col].astype('category').cat.codes

    # Criando DataFrame de despesas
    df_despesas = df[
        [
            'DT_COMPRA',
            'DESPESA',
            'RECEITA_DESPESA',
            'FORMA_PAGTO',
            'TIPO',
            'CATEGORIA',
            'ITEM',
            'VLR_TOTAL',
            'QTD_PARCELAS',
            'VLR_PARCELA',
        ]
    ]

    # Exibindo as primeiras 5 linhas do DataFrame
    print()  # Linha em branco para separar a saída de cada coluna
    print(f'Amostra do arquivo {df_despesas.head()}')

    # Criar um arquivo CSV a partir do DataFrame
    df_despesas.to_csv(caminho_arquivo_saida, index=False)


caminho_arquivo_entrada = './input/lanctos_receitas_despesas.csv'
caminho_arquivo_saida = './output/despesas_receitas.csv'
processar_csv(caminho_arquivo_entrada, caminho_arquivo_saida)
