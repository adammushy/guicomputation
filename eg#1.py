from tkinter import *
from turtle import onclick
root=Tk()

Label(root,text="enter the first number :",bg="white",fg="black").grid(column=1,row=1)
Label(root,text="enter the second number :",bg="white",fg="black").grid(column=1,row=2)
Label(root,text="enter the third number :",bg="white",fg="black").grid(column=1,row=3)
Label(root,text="enter the fourth number :",bg="white",fg="black").grid(column=1,row=4)

num1=IntVar()
num2=IntVar()
num3=IntVar()
num4=IntVar()
Entry(root,textvariable=num1,bg="white",fg="black").grid(column=2,row=1)
Entry(root,textvariable=num2,bg="white",fg="black").grid(column=2,row=2)
Entry(root,textvariable=num3,bg="white",fg="black").grid(column=2,row=3)
Entry(root,textvariable=num4,bg="white",fg="black").grid(column=2,row=4)

def onclick():
    sum=num1.get()+num2.get()+num3.get()+num4.get()
    return ep_lebel.config(text='the sum is '+str(sum))

ep_lebel=Label(root,fg="black")
ep_lebel.grid(column=2,row=6)
Button(root,text='clickme',command=onclick).grid(column=2,row=7)
root.mainloop()
