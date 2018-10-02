from PIL import Image, ImageDraw, ImageFont
import math

font = ImageFont.truetype("arial.ttf", 30)
def center(xc,yc,r,n,k):
    rad=2*math.pi/n*k
    xk=r*math.cos(rad)
    yk=r*math.sin(rad)
    return xc+xk, yc+yk


def drawcrcl(draw,xy,r):
    x,y=xy[0],xy[1]
    if r<0:
        draw.ellipse([x+r,y+r,x-r,y-r],outline='black',fill='white')
    else:
        draw.ellipse([x-r,y-r,x+r,y+r],outline='black',fill='white')
    


def drawcrcls(draw,xc,yc,r,n,rc):
    for i in range(0,n):
        drawcrcl(draw,center(xc,yc,r,n,i),rc)
        draw.text(center(xc,yc,r,n,i),str(i),fill='black',font=font)
        #print(center(xc,yc,r,n,i),rc)

def drawroads(draw,xc,yc,r,n,rm):
    for i in rm:
        draw.line([center(xc,yc,r,n,i.a.idt),center(xc,yc,r,n,i.b.idt)],fill='black')




if __name__=='__main__':
    a=Image.new('RGBA',(1000,1000),color='white')
    d=ImageDraw.Draw(a)












