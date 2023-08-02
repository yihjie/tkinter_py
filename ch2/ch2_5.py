# anchor

from tkinter import *

root = Tk()

root.title('Chapter 2-5 : Anchor')

label_nw = Label(root, text="NW - I like tkinter", fg='blue', bg='yellow', height=3, width=30, anchor='nw').pack()
label_n = Label(root, text="N - I like tkinter", fg='blue', bg='green', height=3, width=30, anchor='n').pack()
label_ne = Label(root, text="NE - I like tkinter", fg='blue', bg='yellow', height=3, width=30, anchor='ne').pack()
label_w = Label(root, text="W - I like tkinter", fg='blue', bg='green', height=3, width=30, anchor='w').pack()
label_center = Label(root, text="Center - I like tkinter", fg='blue', bg='yellow', height=3, width=30, anchor='center').pack()
label_e = Label(root, text="E - I like tkinter", fg='blue', bg='green', height=3, width=30, anchor='e').pack()
label_sw = Label(root, text="SW - I like tkinter", fg='blue', bg='yellow', height=3, width=30, anchor='sw').pack()
label_s = Label(root, text="S - I like tkinter", fg='blue', bg='green', height=3, width=30, anchor='s').pack()
label_se = Label(root, text="SE - I like tkinter", fg='blue', bg='yellow', height=3, width=30, anchor='se').pack()

root.mainloop()