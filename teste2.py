import PySimpleGUI as sg

#Abre uma janela para o usuário selecionar um ficehiro 
path = sg.popup_get_file("Selecione um ficheiro")

#Imprime o caminho do ficheiro selecionado
print(path)
