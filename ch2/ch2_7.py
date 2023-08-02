# wraplength

from tkinter import *

root = Tk()

root.title('Chapter 2-7 : wraplength')

label=Label(root, text="I like tkinter", fg='red', bg='green', height=3, width=15, anchor='nw', wraplength=40)
label.pack()

root.mainloop()