# import pandas as pd
# pip install polars
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/202501_NovoBolsaFamilia.csv'

try:
    inicio = datetime.now()
    print('Obtendo os dados...')
    
    # Pandas
    # df_bolsa_familia = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    
    # Polars
    df_bolsa_familia = pl.read_csv(ENDERECO_DADOS, separator=';', encoding='iso-8859-1')
    print(df_bolsa_familia.head())

    fim = datetime.now()
    print(f'Tempo total de Execução: {fim - inicio}')
    # 0:00:23.846279  //  0:00:16.386841
except Exception as e:
    print('Erro ao obter dados ', e)