from cProfile import label
from tkinter import *
from tkinter import font
from webbrowser import get

root=Tk()
root.geometry('500x300')

def onclick():
    def display():
        info="your age is "+str(age.get())+" and your name is "+name.get()
        el.config(text=info)
        
    Label(root,text="enter your age",font=12,fg="black").grid(row=1,column=0)
    Label(root,text="enter your name",font=12,fg="black").grid(row=2,column=0)
    age=IntVar()
    Entry(root,font=14,fg="black",textvariable=age).grid(row=1,column=1)
    name=StringVar()
    Entry(root,font=14,fg="black",textvariable=name).grid(row=2,column=1)
    Button(root,text="display button",command=display).grid(row=3,column=1)
    el=Label(root,font=12,fg="black")
    el.grid(row=4,column=1)

    
Label(root,text="if you want to start some actions click the button",fg="black",font=13).grid(row=0,column=0)
Button(root,text="control button",command=onclick).grid(row=0,column=1)







root.mainloop()