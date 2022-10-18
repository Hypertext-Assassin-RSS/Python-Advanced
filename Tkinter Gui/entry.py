from tkinter import *
from tkinter import ttk
from turtle import width

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
   global entry1
   name= entry1.get()
   print("Name :",name)
   #label.configure(text=string)

   global entry2
   address = entry2.get()
   print("Address :",address)

   global entry3
   salary = entry3.get()
   print("Salary :",salary)
   
#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
lbl1 = Label(win,text='Name')
lbl1.pack()

entry1= Entry(win, width= 40)
entry1.focus_set()
entry1.pack()

lbl2 = Label(win,text='Address')
lbl2.pack()

entry2 = Entry(win,width=40)
entry2.pack()

lbl3 = Label(win,text="salary")
lbl3.pack()

entry3 = Entry(win,width=40)
entry3.pack()



#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()