# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:57:25 2018

@author: UARTman
"""
import random


dots=[]
roads=[]



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
        
if __name__=='__main__':
    print('Ввод значений: кол-во городов, enter, кол-во ходов')
    print('Вывод: Дорога из:, дорога в:, длина дороги')
    Generate(int(input()),int(input()))
    Visual()
    input()
    
    
    








