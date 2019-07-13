from tkinter import*
flag=0
n=0
root=Tk()
#entr=Entry(width=20)
lbl=Label(root,bg='black',fg='white',width=20)
beq=Button(root,text="=",width=2,height=1)
bpls=Button(root,text="+",width=2,height=1)
bmns=Button(root,text="-",width=2,height=1)
bdiv=Button(root,text="/",width=2,height=1)
bmltp=Button(root,text="*",width=2,height=1)
btn1=Button(root,text="1",width=2,height=1)
btn2=Button(root,text="2",width=2,height=1)
btn3=Button(root,text="3",width=2,height=1)
btn4=Button(root,text="4",width=2,height=1)
btn5=Button(root,text="5",width=2,height=1)
btn6=Button(root,text="6",width=2,height=1)
btn7=Button(root,text="7",width=2,height=1)
btn8=Button(root,text="8",width=2,height=1)
btn9=Button(root,text="9",width=2,height=1)
btn0=Button(root,text="0",width=2,height=1)
btndot=Button(root,text=".",width=2,height=1)
btnclear=Button(root,text="C",width=2,height=1,fg='#ff0000', activeforeground='#ff0000')
#entr.pack(side=TOP)
lbl.grid(row=0,column=1,columnspan=4)
beq.grid(row=4,column=4)
bpls.grid(row=3,column=4)
bmns.grid(row=2,column=4)
bdiv.grid(row=2,column=4)
bmltp.grid(row=1,column=4)
btn1.grid(row=3,column=1)
btn2.grid(row=3,column=2)
btn3.grid(row=3,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=1,column=1)
btn8.grid(row=1,column=2)
btn9.grid(row=1,column=3)
btn0.grid(row=4,column=2)
btndot.grid(row=4,column=3)
btnclear.grid(row=4,column=1)
def one(event):
    lbl['text']=lbl['text']+'1'
def two(event):
   lbl['text']=lbl['text']+'2'
def three(event):
    lbl['text']=lbl['text']+'3'
def four(event):
    lbl['text']=lbl['text']+'4'
def five(event):
    lbl['text']=lbl['text']+'5'
def six(event):
    lbl['text']=lbl['text']+'6'
def seven(event):
    lbl['text']=lbl['text']+'7'
def eight(event):
    lbl['text']=lbl['text']+'8'
def nine(event):
    lbl['text']=lbl['text']+'9'
def zero(event):
    lbl['text']=lbl['text']+'0'
def dot(event):
    if lbl['text']=='':
        lbl['text']=lbl['text']+'0.'
    else:
        lbl['text']=lbl['text']+'.'
def clearall(event):
    lbl['text']=''
def addition(event):
    global n,flag
    n=float(lbl['text'])
    flag=1
    lbl['text']=''

def subtraction(event):
    global n,flag
    n=float(lbl['text'])
    flag=2
    lbl['text']=''

def multiplication(event):
    global n,flag
    n=float(lbl['text'])
    flag = 3
    lbl['text']=''

def division(event):
    global n,flag
    n=float(lbl['text'])
    flag=4
    lbl['text']=''

def equal(event):
    global n,flag
    n1=float(lbl['text'])
    if flag==1:
        lbl['text']=str(n+n1)
    elif flag==2:
        lbl['text']=str(n-n1)
    elif flag==3:
        lbl['text']=str(n*n1)
    elif flag==4:
        lbl['text']=str(n/n1)
    flag=0

btn1.bind('<Button-1>',one)
btn2.bind('<Button-1>',two)
btn3.bind('<Button-1>',three)
btn4.bind('<Button-1>',four)
btn5.bind('<Button-1>',five)
btn6.bind('<Button-1>',six)
btn7.bind('<Button-1>',seven)
btn8.bind('<Button-1>',eight)
btn9.bind('<Button-1>',nine)
btn0.bind('<Button-1>',zero)
btndot.bind('<Button-1>',dot)
bpls.bind('<Button-1>',addition)
bmns.bind('<Button-1>',subtraction)
bmltp.bind('<Button-1>',multiplication)
bdiv.bind('<Button-1>',division)
beq.bind('<Button-1>', equal)
btnclear.bind('<Button-1>',clearall)
root.mainloop()
