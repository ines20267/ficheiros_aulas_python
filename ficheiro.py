import PySimpleGUI as sg
path = sg.popup_get_file('Carregar o ficheiro')
print(path)