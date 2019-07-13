def dectobin(x):
    otpt=''
    while x!=1:
        otpt=str(x%2)+otpt
        x=x//2
    otpt='1'+otpt
    return(otpt)

def bintodec(x):
    otpt=0
    n=len(x)
    for i in range(n):
        otpt+=int(x[i])*2**(n-(i+1))
    return(otpt)

def bintoocto(x):
    otpt=''
    n=len(x)
    for i in range(n//3):
        n=len(x)
        if n>3:
            otpt=str(bintodec(x[(n-3):(n)]))+otpt
        else:
            otpt=str(bintodec(x))+otpt
        x=x[0:(n-3)]
    return(otpt)

def bintohex(x):
    otpt=''
    n=len(x)
    if n%4!=0:
        n+=(4-(n%4))
    for i in range(n//4):
        n=len(x)
        if n>4:
            tmp=bintodec(x[(n-4):(n)])
            if tmp>9:
                if tmp==10:
                    tmp=str(tmp)
                    tmp='A'
                elif tmp==11:
                    tmp=str(tmp)
                    tmp='B'
                elif tmp==12:
                    tmp=str(tmp)
                    tmp='C'
                elif tmp==13:
                    tmp=str(tmp)
                    tmp='D'
                elif tmp==14:
                    tmp=str(tmp)
                    tmp='E'
            otpt=str(tmp)+otpt
        else:
            otpt=str(bintodec(x))+otpt
        x=x[0:(n-4)]
    return(otpt)

