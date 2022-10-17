from optparse import Option
from tkinter import *

class Demo:
    
    window = Tk()
    window.geometry('400x200')

    btn = Button(window,text='Submit')
    btn.pack()

    lbl = Label(window,text='This is label',fg='red')
    lbl.pack()

    chebtn1 = Checkbutton(window,text='Male')
    chebtn1.pack()

    chebtn2 = Checkbutton(window,text='Female')
    chebtn2.pack()
    
    window.mainloop()