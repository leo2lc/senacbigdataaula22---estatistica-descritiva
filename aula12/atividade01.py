import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

# Obtendo os dados e concatenando os meses

try:
    inicio = datetime.now()
    print('Obtendo os dados...')

    df_bolsa_familia = None
    lista_arquivos = ['202503_NovoBolsaFamilia.csv','202504_NovoBolsaFamilia.csv']

    for arquivo in lista_arquivos:
        print(f'Lendo o mês {arquivo}')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')
        print(df.head(5))

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia])

    del df

    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)
    print(df_bolsa_familia.columns)

    fim = datetime.now()
    print(f'Tempo total de Execução {fim - inicio}')


except Exception as e:
    print(f'Erro ao encontrar os meses: {e}')
