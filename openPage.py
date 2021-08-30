from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Url da página'), sg.Input(key='url')],
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
            interval = int(valores['tempo'])
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get(url)
            time.sleep(interval)
            driver.quit()

