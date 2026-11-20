import PySimpleGUI as sg
for i in range(2000):
    sg.one_line_progress_meter(
        'Barra_Progresso',
        i + 1,
        2000,
        'Este teclado de barra de progresso',
        'Isto é uma barra de progresso'
    )