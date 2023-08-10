# widget 共通屬性 relief style
# relief = raised | flat | sunken | groove | ridge | solid
from tkinter import *

root = Tk()
root.title('Chapter 2 - 17 : relief')

label_raised = Label(root, text='raised', relief='raised').pack()
label_flat = Label(root, text='flat', relief='flat', bg='lightyellow').pack()
label_sunken = Label(root, text='sunken', relief='sunken').pack()
label_groove = Label(root, text='groove', relief='groove', bg='lightyellow').pack()
label_ridge = Label(root, text='ridge', relief='ridge').pack()
label_solid = Label(root, text='solid', relief='solid', bg='lightyellow').pack()

root.mainloop()
