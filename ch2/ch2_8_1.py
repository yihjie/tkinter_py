# Font

from tkinter import *

root = Tk()

root.title("Chapter 2-8 : Font")

label = Label(root, text="I like Tkinter", fg='red', bg='green', height=3, width=15, font=("Helvetica", 20, "bold"))
label.pack()

root.mainloop()
