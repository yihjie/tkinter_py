# justify : left, center, right

from tkinter import *

root = Tk()

root.title("Chapter 2-9 : Justify")

label_default = Label(root, text="abcdefghijklmnopqrstuvwxyz", fg='blue', bg='lightyellow', wraplength=80).pack()
label_center = Label(root, text="abcdefghijklmnopqrstuvwxyz", fg='red', bg='navyblue', wraplength=80, justify='center').pack()
label_right = Label(root, text="abcdefghijklmnopqrstuvwxyz", fg='blue', bg='lightyellow', wraplength=80, justify='right').pack()
label_left = Label(root, text="abcdefghijklmnopqrstuvwxyz", fg='red', bg='navyblue', wraplength=80, justify='left').pack()

root.mainloop()
