import pandas as pd


# Função para ler o CSV, realizar transformações e salvar o resultado
def process_despesas(input_path, output_path):
    # Lendo o arquivo CSV
    df = pd.read_csv(input_path, delimiter=';', encoding='utf-8')

    # Exemplo de transformação: Selecionar apenas algumas colunas e renomeá-las
    df_transformed = df[['DT COMPRA', 'DESPESA', 'VLR TOTAL', 'STATUS']].copy()
    df_transformed.columns = ['Data', 'Descrição', 'Valor', 'Status']

    # Exemplo de transformação: Filtrar apenas as despesas pagas
    df_transformed = df_transformed[df_transformed['Status'] == 'Pago']

    # Salvando o DataFrame transformado em um novo arquivo CSV
    df_transformed.to_csv(output_path, index=False, sep=';')


if __name__ == '__main__':
    input_file = './input/lanctos_receitas_despesas.csv'
    output_file = './output/lancamento.csv'
    process_despesas(input_file, output_file)
