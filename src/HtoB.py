from tkinter import*
from random import*
from time import sleep
root = Tk()
root.geometry('550x400')
but = []
for i in range(12):
    but.append(Button(root,width=3,font=("Arial",14,"bold"),text='0'))

count = 0
dec = 0
d = 0

def ch0(event):
    global d
    if but[0]['text']=='0':
        but[0]['text']='1'
        d=d+2**11
    else:
        but[0]['text']='0'
        d=d-2**11

def ch1(event):
    global d
    if but[1]['text']=='0':
        but[1]['text']='1'
        d=d+2**10
    else:
        but[1]['text']='0'
        d=d-2**10

def ch2(event):
    global d
    if but[2]['text']=='0':
        but[2]['text']='1'
        d=d+2**9
    else:
        but[2]['text']='0'
        d=d-2**9

def ch3(event):
    global d
    if but[3]['text']=='0':
        but[3]['text']='1'
        d=d+2**8
    else:
        but[3]['text']='0'
        d=d-2**8

def ch4(event):
    global d
    if but[4]['text']=='0':
        but[4]['text']='1'
        d=d+2**7
    else:
        but[4]['text']='0'
        d=d-2**7

def ch5(event):
    global d
    if but[5]['text']=='0':
        but[5]['text']='1'
        d=d+2**6
    else:
        but[5]['text']='0'
        d=d-2**6

def ch6(event):
    global d
    if but[6]['text']=='0':
        but[6]['text']='1'
        d=d+2**5
    else:
        but[6]['text']='0'
        d=d-2**5

def ch7(event):
    global d
    if but[7]['text']=='0':
        but[7]['text']='1'
        d=d+2**4
    else:
        but[7]['text']='0'
        d=d-2**4

def ch8(event):
    global d
    if but[8]['text']=='0':
        but[8]['text']='1'
        d=d+2**3
    else:
        but[8]['text']='0'
        d=d-2**3

def ch9(event):
    global d
    if but[9]['text']=='0':
        but[9]['text']='1'
        d=d+2**2
    else:
        but[9]['text']='0'
        d=d-2**2

def ch10(event):
    global d
    if but[10]['text']=='0':
        but[10]['text']='1'
        d=d+2
    else:
        but[10]['text']='0'
        d=d-2

def ch11(event):
    global d
    if but[11]['text']=='0':
        but[11]['text']='1'
        d=d+1
    else:
        but[11]['text']='0'
        d=d-1



def chek():
    global count,d,dec,tab
    if d==dec:
        count=count+100
        tab['text']='Счёт:'+str(count)
    else:
        count=count-50
        tab['text']='Счёт:'+str(count)
    for i in range(12):
        but[i]['text']='0'
    d=0
    game()
def f(a):
    if a==10:
        return('A')
    elif a==11:
        return('B')
    elif a==12:
        return('C')
    elif a==13:
        return('D')
    elif a==14:
        return('E')
    elif a==15:
        return('F')
def game():
    global dec
    x=randint(0,15)
    if x>9:
        s1=f(x)
    else:
        s1=str(x)
    y=randint(0,15)
    if y>9:
        s2=f(y)
    else:
        s2=str(y)
    z=randint(0,15)
    if z>9:
        s3=f(z)
    else:
        s3=str(z)
    l1['text']=s1+s2+s3
    dec=x*16*16+y*16+z

l1=Label(root,text='',width=3,font=('Arial',14,"bold"),bg='#00ff00',fg='#ffff00')
l1.grid(row=6,column=4)
b=Button(command=chek,font=('Arial',14,"bold"),bg='#007dff',fg='#00ff00',text='Проверить')
b.grid(row=9,column=3,columnspan=3)
tab=Label(root,text="Счёт:"+str(count),font=('Arial',14,"bold"),fg='#00ff00')
tab.grid(row=1,column=0,columnspan=3)

for i in range(12):
    but[i].grid(row=11,column=i)

but[0].bind('<Button-1>',ch0)
but[1].bind('<Button-1>',ch1)
but[2].bind('<Button-1>',ch2)
but[3].bind('<Button-1>',ch3)
but[4].bind('<Button-1>',ch4)
but[5].bind('<Button-1>',ch5)
but[6].bind('<Button-1>',ch6)
but[7].bind('<Button-1>',ch7)
but[8].bind('<Button-1>',ch8)
but[9].bind('<Button-1>',ch9)
but[10].bind('<Button-1>',ch10)
but[11].bind('<Button-1>',ch11)
game()

root.mainloop()
