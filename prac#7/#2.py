from tkinter import *

root=Tk()
root.geometry("300x300")
Label(root,text="enter your age",font=12,fg="black").grid(row=0,column=0)
Label(root,text="enter your age",font=12,fg="black").grid(row=1,column=0)
Entry(root,font=14,fg="black").grid(row=0,column=1)
Entry(root,font=14,fg="black").grid(row=1,column=1)


root.mainloop()