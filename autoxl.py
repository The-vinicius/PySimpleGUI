import pandas as pd
from datetime import datetime


def read_cliente(arq: str, nome: str):
    df = pd.read_excel(arq)
    for cliente in df['Nome']:
        if nome == cliente:
            result = df[df['Nome'] == nome]
            for v in result.values:
                for i, c in enumerate(result.iloc[:, 1:]):
                    print(f'{c} : {v[i + 1]}')
                print(30 * '_')
            break


def inserir(arq: str, nome: str, modelo: str, price: float):
    hoje = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dados = pd.read_excel(arq)

    if dados.columns[0] == 'Unnamed: 0':
        dados.drop('Unnamed: 0', axis=1, inplace=True)

    dados.loc[dados.shape[0]] = [hoje, nome, modelo, price]
    writer = pd.ExcelWriter(arq, engine='xlsxwriter')
    dados.to_excel(writer, sheet_name='registros')
    writer.save()
