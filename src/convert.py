from tkinter import*
from functools import partial
from binconversion import*
from threading import Timer
from random import randint
root = Tk()
def buttonchange(y1,i):
    global blist,score
    if blist[y1][i]['text']=='0':
        blist[y1][i]['text']='1'
    else:
        blist[y1][i]['text']='0'
    blist[y1][8]['text']=''
    for j in range(8):
        blist[y1][8]['text']=blist[y1][8]['text']+blist[y1][j]['text']
    blist[y1][8]['text']=str(bintodec(blist[y1][8]['text']))
    if blist[y1][8]['text']==blist[y1][9]['text']:
        blist[y1][9]['text']='-'
        score['text']=str(int(score['text'])+100)
    else:
        score['text']=str(int(score['text'])-25)
def addline():
    global tmr,lbllose
    tmp2=0
    y=0
    for tmp in range(0,5):
        if blist[tmp][9]['text']=='-':
            y=tmp
            break
        else:
            tmp2+=1
            if tmp2==5:
                lbllose['text']='YOU LOSE'
                tmr.cancel()
                return()
    for i in range (9):
        blist[y][i]['text']='0'
    blist[y][9]['text']=str(2**randint(0,7))
    tmr=Timer(5.0,addline)
    tmr.start()

def ch0(event):
    global d,but
    if but[0]['text']=='0':
        but[0]['text']='1'
        d=d+2**8
    else:
        but[0]['text']='0'
        d=d-2**8
def ch1(event):
    global d,but
    if but[1]['text']=='0':
        but[1]['text']='1'
        d=d+2**7
    else:
        but[1]['text']='0'
        d=d-2**7
def ch2(event):
    global d,but
    if but[2]['text']=='0':
        but[2]['text']='1'
        d=d+2**6
    else:
        but[2]['text']='0'
        d=d-2**6
def ch3(event):
    global d,but
    if but[3]['text']=='0':
        but[3]['text']='1'
        d=d+2**5
    else:
        but[3]['text']='0'
        d=d-2**5
def ch4(event):
    global d,but
    if but[4]['text']=='0':
        but[4]['text']='1'
        d=d+2**4
    else:
        but[4]['text']='0'
        d=d-2**4
def ch5(event):
    global d,but
    if but[5]['text']=='0':
        but[5]['text']='1'
        d=d+2**3
    else:
        but[5]['text']='0'
        d=d-2**3
def ch6(event):
    global d,but
    if but[6]['text']=='0':
        but[6]['text']='1'
        d=d+2**2
    else:
        but[6]['text']='0'
        d=d-2**2
def ch7(event):
    global d,but
    if but[7]['text']=='0':
        but[7]['text']='1'
        d=d+2
    else:
        but[7]['text']='0'
        d=d-2
def ch8(event):
    global d,but
    if but[8]['text']=='0':
        but[8]['text']='1'
        d=d+1
    else:
        but[8]['text']='0'
        d=d-1
def chek():
    global count,d,dec,tab
    if d==dec:
        count=count+1
        tab['text']='Счёт -> '+str(count)
    else:
        count=count-1
        tab['text']='Счёт -> '+str(count)
    if count>=0:
        game()
def game():
    global dec,lab
    x=randint(1,7)
    y=randint(1,7)
    z=randint(1,7)
    dec=x*8*8+y*8+z
    lab['text']=str(x)+str(y)+str(z)

def ch01(event):
    global d,but
    if but[0]['text']=='0':
        but[0]['text']='1'
        d=d+2**11
    else:
        but[0]['text']='0'
        d=d-2**11
def ch11(event):
    global d,but
    if but[1]['text']=='0':
        but[1]['text']='1'
        d=d+2**10
    else:
        but[1]['text']='0'
        d=d-2**10
def ch21(event):
    global d,but
    if but[2]['text']=='0':
        but[2]['text']='1'
        d=d+2**9
    else:
        but[2]['text']='0'
        d=d-2**9
def ch31(event):
    global d,but
    if but[3]['text']=='0':
        but[3]['text']='1'
        d=d+2**8
    else:
        but[3]['text']='0'
        d=d-2**8
def ch41(event):
    global d,but
    if but[4]['text']=='0':
        but[4]['text']='1'
        d=d+2**7
    else:
        but[4]['text']='0'
        d=d-2**7
def ch51(event):
    global d,but
    if but[5]['text']=='0':
        but[5]['text']='1'
        d=d+2**6
    else:
        but[5]['text']='0'
        d=d-2**6
def ch61(event):
    global d,but
    if but[6]['text']=='0':
        but[6]['text']='1'
        d=d+2**5
    else:
        but[6]['text']='0'
        d=d-2**5
def ch71(event):
    global d,but
    if but[7]['text']=='0':
        but[7]['text']='1'
        d=d+2**4
    else:
        but[7]['text']='0'
        d=d-2**4
def ch81(event):
    global d,but
    if but[8]['text']=='0':
        but[8]['text']='1'
        d=d+2**3
    else:
        but[8]['text']='0'
        d=d-2**3
def ch91(event):
    global d,but
    if but[9]['text']=='0':
        but[9]['text']='1'
        d=d+2**2
    else:
        but[9]['text']='0'
        d=d-2**2
def ch101(event):
    global d,but
    if but[10]['text']=='0':
        but[10]['text']='1'
        d=d+2
    else:
        but[10]['text']='0'
        d=d-2
def ch111(event):
    global d,but
    if but[11]['text']=='0':
        but[11]['text']='1'
        d=d+1
    else:
        but[11]['text']='0'
        d=d-1
def chek1():
    global count,d,dec,tab,but,tab
    if d==dec:
        count=count+100
        tab['text']='Счёт:'+str(count)
    else:
        count=count-50
        tab['text']='Счёт:'+str(count)
    for i in range(12):
        but[i]['text']='0'
    d=0
    game1()
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
def game1():
    global dec,l1
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

def win():
    root.title('Binary Game')
    root.geometry('400x400')
    root['bg'] = '#020233'
    root.iconbitmap('ssyp.ico')

def close_win1():
    global root,blist,score,lbllose
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    root.geometry('1000x600')
    tmr=Timer(5.0,addline)
    blist=[]
    for i in range(5):
        blist.append([])
    for row in range(5):
        for column in range(8):
            blist[row].append(Button(root,font=('Arial', 36, 'bold'), text='0',width=3,command=partial(buttonchange,row,column)))
        Label(root,font=('Arial', 36, 'bold'),width=3,text='-')
        blist[row].append(Label(root,font=('Arial', 36, 'bold'),width=3,bg='#000000',fg='#ffffff',text='0'))
        blist[row].append(Label(root,font=('Arial', 36, 'bold'),width=3,fg='#000000',text='-'))
    for i in range(5):
        for j in range(10):
            blist[i][j].grid(column=j,row=5-i)
    score=Label(root,font=('Arial', 36, 'bold'), height=1,fg='#000000',bg='#ffffff',text='0', width=6)
    lbl1=Label(root,font=('Arial', 36, 'bold'), height=1, text='Score:',bg='#020233',fg='#ffffff')
    lbl2=Label(root,font=('Arial', 36, 'bold'), height=1,bg='#020233',fg='#ffffff',text='Bin To Dec')
    lbllose=Label(root,font=('Comic Sans MS', 36, 'bold','italic','underline'), height=1,fg='#000000',bg='#020233')
    for i in range(5):
        for j in range(10):
            blist[i][j].grid(column=j,row=5-i)
    score.grid(column=2,row=6,columnspan=2)
    lbl1.grid(column=0,row=6,columnspan=2)
    lbllose.grid(column=4,columnspan=3,row=6)
    lbl2.grid(column=7,columnspan=3,row=6)
    addline()

def close_win2():
    global root,but,lab,d,count,tab
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    root['bg'] = '#020233'
    root.geometry('414x150')
    but=[]
    for i in range(9):
        but.append(Button(root,width=3,font=("Arial",14,"bold"),text="0"))
    count=0
    dec=0
    d=0
    lvllab=Label(root,text='Bin To Oct',width=10,font=("Arial",14,"bold"),bg='#020233',fg='#ffffff')
    lvllab.grid(row=1,column=6,columnspan=5)
    lab=Label(root,text='',width=3,font=("Arial",14,"bold"),bg='#00ff00',fg='#ffff00')
    lab.grid(row=6,column=4)
    b=Button(command=chek,font=("Arial",14,"bold"),bg='#007dff', fg='#00ff00', text="Проверить")
    b.grid(row=9,column=3,columnspan=3)
    tab=Label(root,text='Счёт -> '+str(count),font=("Arial",14,"bold"),fg='#00ff00',bg='#020233')
    tab.grid(row=1,column=0,columnspan=3)
    for i in range(9):
        but[i].grid(row=8,column=i)
    but[0].bind('<Button-1>',ch0)
    but[1].bind('<Button-1>',ch1)
    but[2].bind('<Button-1>',ch2)
    but[3].bind('<Button-1>',ch3)
    but[4].bind('<Button-1>',ch4)
    but[5].bind('<Button-1>',ch5)
    but[6].bind('<Button-1>',ch6)
    but[7].bind('<Button-1>',ch7)
    but[8].bind('<Button-1>',ch8)
    game()



def close_win3():
    global root,but,dec,count,d,l1,tab
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    root.geometry('550x130')
    but = []
    for i in range(12):
        but.append(Button(root,width=3,font=("Arial",14,"bold"),text='0'))

    count = 0
    dec = 0
    d = 0


    l1=Label(root,text='',width=3,font=('Arial',14,"bold"),bg='#00ff00',fg='#ffff00')
    l1.grid(row=6,column=4,columnspan=4)
    b=Button(command=chek1,font=('Arial',14,"bold"),bg='#007dff',fg='#00ff00',text='Проверить')
    b.grid(row=9,column=4,columnspan=4)
    tab=Label(root,text="Счёт:"+str(count),font=('Arial',14,"bold"),fg='#00ff00',bg='#020233')
    tab.grid(row=1,column=0,columnspan=3)
    lvlab=Label(root,text='Bin To Hex',font=('Arial',14,"bold"),bg='#020233',fg='#ffffff')
    lvlab.grid(row=1,column=8,columnspan=4)
    for i in range(12):
        but[i].grid(row=11,column=i)

    but[0].bind('<Button-1>',ch01)
    but[1].bind('<Button-1>',ch11)
    but[2].bind('<Button-1>',ch21)
    but[3].bind('<Button-1>',ch31)
    but[4].bind('<Button-1>',ch41)
    but[5].bind('<Button-1>',ch51)
    but[6].bind('<Button-1>',ch61)
    but[7].bind('<Button-1>',ch71)
    but[8].bind('<Button-1>',ch81)
    but[9].bind('<Button-1>',ch91)
    but[10].bind('<Button-1>',ch101)
    but[11].bind('<Button-1>',ch111)
    game1()
    
win()

btn1 = Button(command=close_win1,width = 60,height = 2,text = 'Bin To Dec',font = ('Calibri 25'),bg = 'black',fg = 'yellow',activebackground = 'yellow',activeforeground = 'black')
btn2 = Button(command=close_win2,width = 60,height = 2,text = 'Bin To Oct',font = ('Calibri 25'),bg = 'black',fg = 'orange',activebackground = 'orange',activeforeground = 'black')
btn3 = Button(command=close_win3,width = 60,height = 2,text = 'Bin To Hex',font = ('Calibri 25'),bg = 'black',fg = 'red',activebackground = 'red',activeforeground = 'black')



btn1.pack(pady = 10,expand = 1)
btn2.pack(pady = 10,expand = 1)
btn3.pack(pady = 10,expand = 1)

root.mainloop()
        
