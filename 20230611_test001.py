# -*- coding: utf-8 -*-

'''
【更新記録】
20230612 新規作成
'''

import io
import os
import sys
import tkinter as tk
import PySimpleGUI as sg

# カレントディレクトリを実行パスにする。
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. レイアウト
canvas = sg.Canvas(size=(200,200) ,background_color = 'grey', key='meow')
layout = [[canvas]]


# 2. ウィンドウの生成
window = sg.Window(
    title='Window title',
    layout=layout
)
window.finalize()

#window['meow'].bind('<Button1-Motion>', '_Nyago')
window['meow'].bind('<Button-1>', '_leftClick')
window['meow'].bind('<Button-3>', '_rightClick')


# 矢印線を描画
# canvas.tk_canvas.create_line(10, 50, 190, 50, fill='red', arrow=tk.FIRST)
# canvas.tk_canvas.create_line(10, 100, 190, 100, fill='red', arrow=tk.LAST)
# canvas.tk_canvas.create_line(10, 150, 190, 150, fill='red', arrow=tk.BOTH)

# 3. GUI処理
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or None:
            break
    
    elif event == 'meow_Nyago':
            print('meow_Nyago', canvas.user_bind_event.x, canvas.user_bind_event.y)

    elif event == 'meow_leftClick':
            print('leftClick', canvas.user_bind_event.x, canvas.user_bind_event.y)

    elif event == 'meow_rightClick':
            print('rightClick', canvas.user_bind_event.x, canvas.user_bind_event.y)

window.close()

sys.exit()

'''
【参考】
20220803【備忘録的な】PySimpleGUIのCanvas要素内でカーソルを追跡する
https://scuser.hatenablog.jp/entry/2022/08/03/214028

'''
