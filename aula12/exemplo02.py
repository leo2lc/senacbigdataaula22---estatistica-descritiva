# import pandas as pd
# pip install polars
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

# Obtendo os dados e concatenando os meses
try:
    inicio = datetime.now()
    print('Obtendo os dados...')

    df_bolsa_familia = None
    lista_arquivos = ['202501_NovoBolsaFamilia.csv', '202502_NovoBolsaFamilia.csv']

    for arquivo in lista_arquivos:
        print(f'Lendo o mês {arquivo}')
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding='iso-8859-1') # Pandas './../DADOS/202501_NovoBolsaFamilia.csv'
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1') # Polars './../DADOS/202501_NovoBolsaFamilia.csv'
        print(df.head(5))

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

    del df

    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape) # Métodos do Polars
    print(df_bolsa_familia.columns) # Métodos do Polars

    fim = datetime.now()
    print(f'Tempo total de Execução: {fim - inicio}')
# 0:01:23.431908 // 0:00:33.906173

except Exception as e:
    print(f'Erro ao encontrar os meses: {e}')
