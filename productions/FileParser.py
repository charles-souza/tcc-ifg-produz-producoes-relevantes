from pandas import DataFrame, read_csv
import pandas as pd

if __name__ == '__main__':
    csv = r'../data/entrada.csv'
    df = pd.read_csv(csv, sep=';')

    ano = df['Ano'].iloc[0]
    print(ano)

    tipoProducao = df['Tipo da Produção'].iloc[0]
    print(tipoProducao)

    arq = r'../data/colunas.csv'
    col = pd.read_csv(arq, sep=';', header=None)
    peso = col.copy()
    peso = peso.loc[[1]]
    col = col.loc[[0]]

    print(col)
    print(peso)

    dir = r'../data/' + str(ano) + '.xls'
    df = pd.read_excel(dir)

    dfLimpo = df.copy()
    dfLimpo = dfLimpo.drop(columns=['Identificador do PPG', 'Código do PPG', 'Nome do PPG', 'Área de Avaliação', 'IES Sigla', 'IES Nome'])
    print(dfLimpo.columns)

    productions = dfLimpo.copy()
    del productions['Item de Detalhamento']
    del productions['Valor do Item de Detalhamento']
    productions = productions.drop_duplicates(['ID da Produção'])

    for index, row in df.iterrows():
        column_name = row['Item de Detalhamento']
        column_value = row['Valor do Item de Detalhamento']
        productions.loc[productions['ID da Produção'] == row['ID da Produção'], column_name] = column_value

    bib_productions = productions[productions['Tipo de Produção'] == 'BIBLIOGRÁFICA']
    bib_productions = bib_productions.dropna(axis=1, how='all')
    tec_productions = productions[productions['Tipo de Produção'] == 'TÉCNICA']
    tec_productions = tec_productions.dropna(axis=1, how='all')
    art_productions = productions[productions['Tipo de Produção'] == 'ARTÍSTICO-CULTURAL']
    art_productions = art_productions.dropna(axis=1, how='all')

    print(bib_productions.columns)

    dicionarioTipoProducao = {1: 'BIBLIOGRÁFICA', 2: 'TÉCNICA', 3: 'ARTÍSTICO-CULTURAL'}
    print(dicionarioTipoProducao)

    if tipoProducao == dicionarioTipoProducao.get(1):
        bib_productions = bib_productions[bib_productions['Ano da Produção'].eq(ano)]
        print(bib_productions.columns)
    elif tipoProducao == dicionarioTipoProducao.get(2):
        tec_productions = tec_productions[tec_productions['Ano da Produção'].eq(ano)]
        tec_productions = tec_productions[tec_productions[col]]
        print(tec_productions.columns)
    elif tipoProducao == dicionarioTipoProducao.get(3):
        art_productions = art_productions[art_productions['Ano da Produção'].eq(ano)]
        print(art_productions.columns)





