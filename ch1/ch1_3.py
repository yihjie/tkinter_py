# 建立視窗，並修改相關屬性
'''
title()
gemoetry(width x height + x + y)
maxsize(width, height)
minsize(width, height)
configure(bg='color')
resizable(width=True, height=True)
state('zoomed')
iconify()
iconbitmap('xx.ico')
'''

from tkinter import *

root = Tk()

root.title("My TK Window")
root.geometry("300x160")
root.configure(bg="#00ff00")
root.iconbitmap('mystar.ico')

root.mainloop()
