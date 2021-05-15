import PySimpleGUI as sg
import autoxl as at
from criarplanilha import *


def telainicial():
    sg.theme('Black')
    layout = [
        [sg.Text('Nome', size=(10, 1)), sg.Input(key='Nome', size=(20, 1))],
        [sg.Text('Modelo', size=(10, 1)), sg.Input(key='model', size=(20, 1))],
        [sg.Text('Preço'), sg.Input(key='price', size=(20, 1))],
        [sg.Button('Salvar'), sg.Button('ver clientes')],
    ]
    return sg.Window('tela', layout=layout, finalize=True)


def get_clientes():
    sg.theme('Black')
    layout = [
        [sg.Text('Nome do cliente', size=(15, 1)), sg.Input(key='get', size=(20, 1))],
        [sg.Text('Clientes', size=(10, 1)), sg.Output(size=(30, 5))],
        [sg.Button('Buscar'), sg.Button('voltar')],
    ]
    return sg.Window('get', layout=layout, finalize=True)


janela1, janela2 = telainicial(), None

arq = 'test.xlsx'
if not verificar(arq):
    criar_xlsx(arq)

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    elif window == janela1 and event == 'Salvar':
        at.inserir(arq, values['Nome'], values['model'], values['price'])
    elif window == janela1 and event == 'ver clientes':
        janela2 = get_clientes()
        janela1.hide()
    elif window == janela2 and event == 'Buscar':
        at.read_cliente(arq, values['get'])
    elif window == janela2 and event == 'voltar':
        janela2.hide()
        janela1.un_hide()
