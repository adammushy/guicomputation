from tkinter import *

root=Tk()
root.geometry("250x50+200+50")
root.title("add numbers")
def add():
    sum=num1.get()+num2.get()
    el.config(text=str(sum))

Label(root,text="number1",font=12,fg="black").grid(row=0,column=0)
Label(root,text="number2",font=12,fg="black").grid(row=1,column=0)
num1=IntVar()
num2=IntVar()
Entry(root,font=14,fg="black",textvariable=num2).grid(row=0,column=1)
Entry(root,font=14,fg="black",textvariable=num1).grid(row=1,column=1)

Button(root,text="display button",command=add).grid(row=3,column=1)


el=Label(root,font=12,fg="black")
el.grid(row=4,column=1)


root.mainloop()