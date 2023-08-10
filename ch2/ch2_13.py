# bitmaps
# error,    hourglass,  info,   questhead,  question
# warning, gray12,      gray25, gray50,     gray75


from tkinter import *

root = Tk()

root.title("Chapter 2-13 : bitmap")

label_error = Label(root, bitmap='error', bg='lightyellow').pack()
label_hourglass = Label(root, bitmap='hourglass', bg='pink').pack()
label_info = Label(root, bitmap='info', bg='lightyellow').pack()
label_questhead = Label(root, bitmap='questhead', bg='pink').pack()
label_question = Label(root, bitmap='question', bg='lightyellow').pack()
label_warning = Label(root, bitmap='warning', bg='pink').pack()
label_gray12 = Label(root, bitmap='gray12', bg='lightyellow').pack()
label_gray25 = Label(root, bitmap='gray25', bg='pink').pack()
label_gray50 = Label(root, bitmap='gray50', bg='lightyellow').pack()
label_gray75 = Label(root, bitmap='gray75', bg='pink').pack()

root.mainloop()
