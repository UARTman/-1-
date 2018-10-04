# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:41:56 2018

@author: UARTman
"""
import Main
from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk

root=Tk()

DEntry = Entry(root)
REntry = Entry(root)
DLabel = Label(root,text='Города')
RLabel = Label(root,text='Дороги')
Submit = Button(root,text='Сгенерировать!')

DEntry.grid(row=1,column=1)
REntry.grid(row=2,column=1)
DLabel.grid(row=1,column=2)
RLabel.grid(row=2,column=2)
Submit.grid(row=3,column=1,columnspan=2)
#ImLabel.grid(row=4,column=1,columnspan=11)



def Do(event):
    root1=Toplevel(root)
    ImLabel = Label(root1)
    Main.Main(int(DEntry.get()),int(REntry.get()))
    a=Image.open('Output.png')
    a = a.resize((600,600), Image.ANTIALIAS)
    b=ImageTk.PhotoImage(a)
    ImLabel.configure(image=b)
    ImLabel.image=b
    ImLabel.pack()
    
    
Submit.bind('<Button-1>',Do)

root.mainloop()