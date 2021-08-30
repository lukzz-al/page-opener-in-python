import webbrowser
import os
import time
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Url da página'), sg.Input(key='url')],
    [sg.Text('Caminho do Browser'), sg.Input(key='caminho')],
    [sg.Text('Intervalo (segundos)'), sg.Input(key='tempo', size=(10,1))],
    [sg.Button('Iniciar')],
]

janela = sg.Window('Browser Page Openner', layout)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
       break

    if eventos == 'Iniciar':
        while True:
            
            url = valores['url']
            path = valores['caminho']
            interval = int(valores['tempo'])

            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
            webbrowser.get('chrome').open(url)
            time.sleep(interval)
            os.system("taskkill/im chrome.exe")
            time.sleep(interval) 

