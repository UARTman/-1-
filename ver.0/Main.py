# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:57:25 2018

@author: UARTman
"""
import random
import ImgDraw

dots=[]
roads=[]

minl=-1
minm=[]


class Dot:
    def __init__(self,idt):
        self.idt=idt
        self.roads=[]


class Road:
    def __init__(self,a,b,l):
        self.a=a
        self.b=b
        self.l=l
        a.roads.append(self)
        b.roads.append(self)
    def oend(self,dot):
        return dots[self.a.idt+self.b.idt-dot.idt]


def genlen(minn=1,maxx=10):
    return random.randrange(minn,maxx+1)

def RandRoads(dot,mx,m=-1):
    x=dots[:]
    x.remove(dot)
    for i in dot.roads:
        x.remove(i.oend(dot))
    k=len(x)
    c=0
    if k:
        if m==-1:
            if 1-(len(dot.roads)%1) == min(k,mx)+1:
                m=min(k,mx)+1
            else:
                m=random.randrange(1-(len(dot.roads)%1),min(k,mx)+1)        
        for i in range(0,m):
            l=random.randrange(0,len(x))
            ll=x[l]
            roads.append(Road(dot,ll,genlen()))
            x.pop(l)
            c+=1
    return c



def Generate(d,r):
    global dots,roads
    dots=[]
    roads=[]
    rr=r
    for i in range(0,d):
        dots.append(Dot(i))
        r-=RandRoads(dots[i],1,1)
    while r:
        for i in dots:
            if r==0:
                break
            r-=RandRoads(i,r,1)
    return rr==len(roads)

            
def Visual():
    for i in roads:
        print(i.a.idt,' ',i.b.idt,' ',i.l)
        

def VDTS(x):
    for i in x:
        print(i.idt)
        
def VDTSG(x,draw):
    ImgDraw.drawroads(draw,500,500,200,len(x),roads)
    ImgDraw.drawcrcls(draw,500,500,200,len(x),30)
        
def GoThrough(a,b,m=[],l=0):
    global minl,minm
    if not len(m):
        m.append(a)
    if minl>=0 and l>=minl:
        return 0
    else:
        if a==b:
            minm=m[:]
            minl=l
            return 1
        for i in a.roads:
            if i.oend(a) in m:
                continue
            m1=m[:]
            m1.append(i.oend(a))
            l1=l
            l1+=i.l
            GoThrough(i.oend(a),b,m=m1,l=l1)
        

    
    
    
if __name__=='__main__':
    print('Ввод значений: кол-во городов, enter, кол-во ходов')
    print('Вывод: Дорога из:, дорога в:, длина дороги')
    Generate(int(input()),int(input()))
    Visual()
    '''
    print('Введите номер пункта А, enter, номер пункта B')
    a=int(input())
    b=int(input())
    GoThrough(dots[a],dots[b])
    print('Длина оптимального маршрута', minl)
    print('Перечень городов в маршруте:')
    VDTS(minm)'''
    print('Все маршруты: точка из, точка в, длина')
    paths=[]
    for i in dots:
        for j in dots:
            if i!=j:
                minl=-1
                minm=[]
                GoThrough(i,j,[])
                paths.append((i,j,minl,minm))
    
    for i in paths:
        print('==========')
        print(i[0].idt,i[1].idt,i[2])
        VDTS(i[3])
    
    a=ImgDraw.Image.new('RGBA',(1000,1000),color='white')
    d=ImgDraw.ImageDraw.Draw(a)
    VDTSG(dots,d)
    del d
    a.show()
    
    
    
    
    input('press enter to exit')
    


    








