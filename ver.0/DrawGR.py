# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:56:34 2018

@author: UARTman
"""
import math
import PIL
import aggdraw
_w,_h,_r=500,500,100
def dncntr(n,k):
    lx=_r*math.cos(k*(math.pi*2/n))
    ly=_r*math.sin(k*(math.pi*2/n))
    return (_w/2+lx,_h/2+ly)


def circle(img,c,r,pen):
    img.ellipse((c[0]+r,c[1]+r,c[0]-r,c[1]-r),pen)


def mcrk(img,n,r,pen):
    for i in range(0,n):
        circle(img,dncntr(n,i),r,pen)

a=PIL.Image.new('RGBA',(500,500),(0,0,0,0))
d=aggdraw.Draw(a)
p=aggdraw.Pen('Black',0.5)
#b = aggdraw.Brush('White')
mcrk(d,5,10,p)
d.flush()
