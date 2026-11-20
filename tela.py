import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        Layout = [
        [sg.Text('Escreva o seu nome'),sg.Input()],
        [sg.Text('Escreva a sua idade'),sg.Input()],
        [sg.Button('Enviar estes dados')]
        ]

        #Janela
        janela = sg.Window("Dados do utilizador").layout(Layout)

        #Extrair os dados da Tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.Iniciar()
