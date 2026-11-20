import PySimpleGUI as sg
for i in range(1, 3000):
    sg.one_line_progress_meter(
        'barra_progresso',
        i + 1,
        3000,
        'este teclado da barra de progresso',
        'isto é uma barra de progresso',
        orientation='h',
        bar_color=("#046804", "#010806")
    )