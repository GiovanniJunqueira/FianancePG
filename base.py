from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import *

#janela principal
def janelabase():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('Seja bem vindo ao seu aplicativo de controle financeiro!')],
        [sg.Text('O que deseja fazer hoje?')],
        [sg.Button('Registrar ENTRADA'), sg.Text ('                 '), sg.Button('Registrar SAÍDA')],
    ]
    return sg.Window('Finance',layout, finalize=True)

#janela entrada
def janela_entrada():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('Qual o valor da entrada?'), sg.Input(key="valorent")],
        [sg.Text('Qual origem da entrada?'), sg.Input(key="origement")],
        [sg.Button('Pronto!')]
    ]
    return sg.Window('Dados Entrada', layout, finalize=True)

#janela saída
def janela_saida():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('Qual o valor da saída?'), sg.Input(key="valorsaida")],
        [sg.Text('Qual tipo de saída?'), sg.Input(key="tiposaida")],
        [sg.Button('Pronto!')]
    ]
    return sg.Window('Dados Saída', layout, finalize=True)

#Abrir janela inicial
janela1, janela2, janela3 = janelabase(), None, None

#loop de eventos
while True:
    window, eventos, valores = sg.read_all_windows()
    #para fexhar a janela se apertar no x
    if window == janela1 and eventos == sg.WINDOW_CLOSED:
        break
    #ir para janela entrada
    if window == janela1 and eventos == 'Registrar ENTRADA':
        janela2=janela_entrada()
        janela1.hide()
    #fechar janela2 
    if window == janela2 and eventos == sg.WINDOW_CLOSED:
        break
    #ir para janela saida
    if window == janela1 and eventos == 'Registrar SAÍDA':
        janela3=janela_saida()
        janela1.hide()
    #fechar janela3
    if window == janela3 and eventos == sg.WINDOW_CLOSED:
        break  
