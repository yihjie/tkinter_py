# 視窗初始畫面在螢幕中央

from tkinter import *

root = Tk()

# 取得螢幕寬度跟高度
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

width = 300
height = 160
x = int((screenWidth - width) / 2)
y = int((screenHeight - height) / 2)

root.geometry(f"{width}x{height}+{x}+{y}")

root.mainloop()
