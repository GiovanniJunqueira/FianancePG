from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import *
from sqlite3 import *
import sqlite3
import dados

#janela principal
def janelabase():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('Seja bem vindo ao seu aplicativo de controle financeiro!')],
        [sg.Text(' ')],
        [sg.Text('Seu saldo total é:'), sg.Text(key='VALORTOTAL')],
        [sg.Text('O valor da ultima entrada registrada foi: R$'), sg.Text(key='valorultentradas')],
        [sg.Text('O valor da ultima saída registrada foi: R$'), sg.Text(key='valorultsaidas')],
        [sg.Text(' ')],
        [sg.Text('O que deseja fazer hoje?')],
        [sg.Button('Registrar ENTRADA'), sg.Button('Zerar saldo total'), sg.Button('Registrar SAÍDA')],
    ]
    return sg.Window('Finance',layout, finalize=True)

#janela entrada
def janela_entrada():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text('Qual o valor da entrada?'), sg.Input(key="valorent")],
        [sg.Text('Qual origem da entrada?'), sg.Input(key="origement")],
        [sg.Button('Pronto')]
    ]
    return sg.Window('Dados Entrada', layout, finalize=True)
 
#função para o valor total
def update_valor_total(window):
    sum_entradas = dados.get_sum_entradas()
    sum_saidas = dados.get_sum_saidas()
    saldo_total = sum_entradas - sum_saidas
    window['VALORTOTAL'].update(f'R$ {saldo_total}')

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
update_valor_total(janela1)

#loop de eventos
while True:
    window, eventos, valores = sg.read_all_windows()
    #para fechar a janela se apertar no x
    if window == janela1 and eventos == sg.WINDOW_CLOSED:
        break
    #ir para janela entrada
    if window == janela1 and eventos == 'Registrar ENTRADA':
        janela2=janela_entrada()
        janela1.close()

    #fechar janela2 
    if window == janela2 and eventos == sg.WINDOW_CLOSED:
        break

    #ir para janela saida
    if window == janela1 and eventos == 'Registrar SAÍDA':
        janela3=janela_saida()
        janela1.close()

    #fechar janela3
    if window == janela3 and eventos == sg.WINDOW_CLOSED:
        break  

    #voltar para o menu inicial
    if window ==janela2 and eventos== 'Pronto':
        janela2.close()
        janela1 = janelabase()
        
        #testar jogar para o banco de dados
        VE = valores["valorent"]
        if VE != '':
            dados.write_entrada(VE)
        janela1['valorultentradas'].update(valores['valorent'])
        update_valor_total(janela1)
#window.find_element("valorent").update(VE)
    

    #voltar para o menu inicial
    if window == janela3 and eventos== 'Pronto!':
        janela3.close()
        janela1 = janelabase()
        janela1['valorultsaidas'].update(valores['valorsaida'])
        VS = valores["valorsaida"]
        if VS != '':
            dados.write_saida(VS)
        update_valor_total(janela1)

#funções para deletar os dados
    if window == janela1 and eventos == 'Zerar saldo total':
        dados.delete_saidas()
        dados.delete_entradas()
        update_valor_total(janela1)


#atribuindo valor 
#valortotal = 0 
#valortotal = int(valores["valorent"]) + valortotal
#janela1['VALORTOTAL'].update(valortotal)


