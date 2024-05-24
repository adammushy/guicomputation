from tkinter import *
from turtle import onclick
root=Tk()
root.geometry("300x300")
def onclick(number):
    e.delete(0,END)
    e.insert(0,number)
    
number=IntVar()
e=Entry(root,textvariable=number,borderwidth=10,width=48)
e.grid(row=0,column=0,columnspan=3)
Button(root,text='7',command=lambda:onclick(7),padx=40).grid(row=1,column=0)
Button(root,text='6',command=lambda:onclick(6),padx=40).grid(row=2,column=0)

Button(root,text='3',command=lambda:onclick(3),padx=40).grid(row=3,column=0)
Button(root,text='0',command=lambda:onclick(0),padx=40).grid(row=4,column=0)
Button(root,text='+',command=lambda:onclick(),padx=40).grid(row=5,column=0)
Button(root,text='8',command=lambda:onclick(8),padx=40).grid(row=1,column=1)
Button(root,text='5',command=lambda:onclick(5),padx=40).grid(row=2,column=1)
Button(root,text='2',command=lambda:onclick(2),padx=40).grid(row=3,column=1)
Button(root,text='clear',padx=90).grid(row=4,column=1,columnspan=2)
Button(root,text='=',padx=40).grid(row=5,column=1)
Button(root,text='9',command=lambda:onclick(9),padx=40).grid(row=1,column=2)
Button(root,text='4',command=lambda:onclick(4),padx=40).grid(row=2,column=2)
Button(root,text='1',command=lambda:onclick(1),padx=40).grid(row=3,column=2)



root.mainloop()
