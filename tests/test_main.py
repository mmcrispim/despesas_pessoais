from io import StringIO

import pandas as pd

from despesas_pessoais.main import process_despesas


def test_process_despesas():
    # Exemplo de conteúdo do CSV
    csv_data = """DT COMPRA;DESPESA;RECEITA DESPESA;FORMA PAGTO;TIPO;CATEGORIA;ITEM;VLR TOTAL;QTD PARCELAS;NUM PARCELA;STATUS;DESCRICAO;;;
    20/07/2010;Jornal O Estado de São Paulo;Despesa;D‚bito Agendado;Gasto;Assinaturas;Jornal;473,40;6;1;Pago;Assinatura Jornal Estado de São Paulo;;;
    20/07/2010;Jornal O Estado de São Paulo;Despesa;D‚bito Agendado;Gasto;Assinaturas;Jornal;473,40;6;2;Pago;Assinatura Jornal Estado de São Paulo;;;
    20/07/2010;Jornal O Estado de São Paulo;Despesa;D‚bito Agendado;Gasto;Assinaturas;Jornal;473,40;6;3;Pendente;Assinatura Jornal Estado de São Paulo;;;
    """

    # Usando StringIO para simular o arquivo CSV
    input_data = StringIO(csv_data)

    # DataFrame esperado após transformação
    expected_output = pd.DataFrame(
        {
            'Data': ['20/07/2010', '20/07/2010'],
            'Descrição': [
                'Jornal O Estado de São Paulo',
                'Jornal O Estado de São Paulo',
            ],
            'Valor': [473.40, 473.40],
            'Status': ['Pago', 'Pago'],
        }
    )

    print(f'saida experada {expected_output}')

    # Chama a função com o CSV simulado
    output_data = StringIO()
    process_despesas(input_data, output_data)

    # Lê o resultado do output_data para um DataFrame
    output_data.seek(0)  # Reset StringIO cursor
    result_df = pd.read_csv(output_data, delimiter=';')

    print(f'retorno {result_df}')

    # Verifica se o resultado está de acordo com o esperado
    pd.testing.assert_frame_equal(result_df, expected_output)
