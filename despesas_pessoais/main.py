import pandas as pd

# Caminho para o arquivo CSV
caminho_arquivo = './input/lanctos_receitas_despesas.csv'

print(f'Caminho {caminho_arquivo}')

# Leitura do arquivo CSV
df = pd.read_csv(caminho_arquivo, header=0, sep=';')

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

# Lista de colunas para as quais você deseja obter valores distintos
colunas = [
    'RECEITA_DESPESA',
    'FORMA_PAGTO',
    'TIPO',
    'CATEGORIA',
    'ITEM',
    'STATUS',
]

# Dicionário para armazenar os DataFrames com valores distintos de cada coluna
valores_distintos = {
    coluna: df[coluna].drop_duplicates() for coluna in colunas
}

# Exibir os valores distintos de cada coluna
for coluna, valores in valores_distintos.items():
    print(f"Valores distintos na coluna '{coluna}':")
    print(valores)
    print()  # Linha em branco para separar a saída de cada coluna

