# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:41:56 2018

@author: UARTman
"""
import Main
from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk,ImageDraw,ImageFont

root=Tk()
font = ImageFont.truetype("arial.ttf", 30)
DEntry = Entry(root)
REntry = Entry(root)
DLabel = Label(root,text='Города')
RLabel = Label(root,text='Дороги')
Submit = Button(root,text='Сгенерировать!')
NameEntry = Entry(root)
NameLabel = Label(root,text='Имя графа')
SaveButton = Button(root,text='Сохранить Граф')
dt,r=0,0


DEntry.grid(row=1,column=1)
REntry.grid(row=2,column=1)
DLabel.grid(row=1,column=2)
RLabel.grid(row=2,column=2)
Submit.grid(row=3,column=1,columnspan=2)
#ImLabel.grid(row=4,column=1,columnspan=11)
NameEntry.grid(row=4,column=1)
NameLabel.grid(row=4,column=2)
SaveButton.grid(row=5,column=1,columnspan=2)


def Do(event):
    global dt,r
    root1=Toplevel(root)
    ImLabel = Label(root1)
    dt,r=DEntry.get(),REntry.get()
    Main.Main(int(dt),int(r))
    a=Image.open('Output.png')
    a = a.resize((600,600), Image.ANTIALIAS)
    b=ImageTk.PhotoImage(a)
    ImLabel.configure(image=b)
    ImLabel.image=b
    ImLabel.pack()

def Save(event):
    global dt,r
    a=Image.open('Output.png')
    d=ImageDraw.Draw(a)
    d.text((0,0),dt+'-'+r+'-'+NameEntry.get(),font=font,fill='black')
    del d
    a.save(dt+'-'+r+'-'+NameEntry.get()+'.png','PNG')
    with open(dt+'-'+r+'-'+NameEntry.get()+'-решения.txt','w') as f:
        print('Решения задачи '+dt+'-'+r+'-'+NameEntry.get()+':',file=f)
        Main.Resh(f,Main.paths)
Submit.bind('<Button-1>',Do)
SaveButton.bind('<Button-1>',Save)
root.mainloop()