# Label
from tkinter import *

root = Tk()

root.title("Chapter 2-1")
label = Label(root, text="I like tkinter")
label.pack()
print(type(label))

root.mainloop()
