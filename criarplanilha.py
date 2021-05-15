from openpyxl import Workbook

# vereficar se existe o xlsx
def verificar(arq: str):
    try:
        arquivo = open(arq, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False  # não existe
    else:
        return True  # existe


def criar_xlsx(arq: str):
    arquivo_excel = Workbook()
    planilha1 = arquivo_excel.active
    planilha1.title = 'registros'
    colunas = ['Data', 'Nome', 'Modelo', 'Preço']
    dados = ['A1', 'B1', 'C1', 'D1']
    for i in range(4):
        planilha1[dados[i]] = colunas[i]
    arquivo_excel.save(arq)
