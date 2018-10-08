# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:41:56 2018

@author: UARTman
"""
import Main
from tkinter import Entry,Label,Button,Tk,Toplevel
from tkinter.ttk import Entry,Label,Button
from PIL import Image,ImageTk,ImageDraw,ImageFont

import os

file_path = "Result/"
directory = os.path.dirname(file_path)

try:
    os.stat(directory)
except:
    os.mkdir(directory)  



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
CountEntry = Entry(root)
CountButton = Button(root,text='Создать n задач')
CountLabel = Label(root,text='Кол-во задач')
dt,r=0,0


DEntry.grid(row=1,column=1)
REntry.grid(row=2,column=1)
DLabel.grid(row=1,column=2)
RLabel.grid(row=2,column=2)
#Submit.grid(row=3,column=1,columnspan=2)
#ImLabel.grid(row=4,column=1,columnspan=11)
#NameEntry.grid(row=4,column=1)
#NameLabel.grid(row=4,column=2)
#SaveButton.grid(row=5,column=1,columnspan=2)
CountLabel.grid(row=3,column=2)
CountEntry.grid(row=3,column=1)
CountButton.grid(row=4,column=1,columnspan=2)
'''
CountLabel.grid(row=6,column=2)
CountEntry.grid(row=6,column=1)
CountButton.grid(row=7,column=1,columnspan=2)
'''

def Do(event,show=True):
    global dt,r
    dt,r=DEntry.get(),REntry.get()
    Main.Main(int(dt),int(r))
    if show:
        root1=Toplevel(root)
        ImLabel = Label(root1)
        a=Image.open('Output.png')
        a = a.resize((600,600), Image.ANTIALIAS)
        b=ImageTk.PhotoImage(a)
        ImLabel.configure(image=b)
        ImLabel.image=b
        ImLabel.pack()

def Save(event,NAME=''):
    global dt,r
    a=Image.open('Output.png')
    d=ImageDraw.Draw(a)
    if NAME=='':
        NAME=NameEntry.get()
    d.text((0,0),dt+'-'+r+'-'+NAME,font=font,fill='black')
    del d
    a.save('Result/'+dt+'-'+r+'-'+NAME+'.png','PNG')
    with open('Result/'+dt+'-'+r+'-'+NAME+'-решения.txt','w') as f:
        print('Решения задачи '+dt+'-'+r+'-'+NAME+':',file=f)
        Main.Resh(f,Main.paths)

def Cycles(event):
    for i in range(1,int(CountEntry.get())+1):
        Do(None,False)
        Save(None,str(i))
    print('Готово!')
Submit.bind('<Button-1>',Do)
SaveButton.bind('<Button-1>',Save)
CountButton.bind('<Button-1>',Cycles)
root.mainloop()