from logging import root
from tkinter import *
root=Tk()
root.geometry("300x300")

def display():
    el.config(text="my name is "+name.get())

Label(root,text="enter your age",font=12,fg="black").grid(row=0,column=0)
name=StringVar()
Entry(root,font=14,fg="black",textvariable=name).grid(row=0,column=1)
Button(root,text="display button",command=display).grid(row=3,column=1)

el=Label(root,font=12,fg="black")
el.grid(row=4,column=1)

root.mainloop()