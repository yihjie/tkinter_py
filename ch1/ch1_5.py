from tkinter import *

width = 300
height = 160
x = 400
y = 200

root = Tk()

root.geometry("%dx%d+%d+%d" % (width, height, x, y))
# root.geometry(f"{width}x{height}+{x}+{y}")

root.mainloop()
