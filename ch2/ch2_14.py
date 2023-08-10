# 圖文共存
# compound = left | right | top | bottom | center

from tkinter import *

root = Tk()
root.title('Chapter 2 - 14 : compound')

label_left = Label(root, bitmap='hourglass', compound='left', text='我的天空').pack()
label_right = Label(root, bitmap='hourglass', compound='right', text='我的天空', bg='lightyellow').pack()
label_top = Label(root, bitmap='hourglass', compound='top', text='我的天空').pack()
label_bottom = Label(root, bitmap='hourglass', compound='bottom', text='我的天空', bg='lightyellow').pack()
label_center = Label(root, bitmap='hourglass', compound='center', text='我的天空').pack()

root.mainloop()
