from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import *

#janela principal
def janelabase():
    sg.theme('DarkBlue4')
    layout = [
       [sg.Text('Qual o valor da entrada?'), sg.Input(key='t')],
       [sg.Button('Pronto'), sg.Text(key='OUTPUT')],
    ]
    return sg.Window('Finance',layout, finalize=True)
teste = values="valorent"
janela1 = janelabase()
#loop de eventos
while True:
    window, eventos, valores = sg.read_all_windows()
    #para fexhar a janela se apertar no x
    if window == janela1 and eventos == sg.WINDOW_CLOSED:
        break
    if eventos=='Pronto':
        window['OUTPUT'].update(valores['t'])