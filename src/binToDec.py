def BintoDec(s):
    d=0
    n=len(s)
    for i in range(n):
        if s[i]=='1':
            d=2**(n-(i+1))+d
    return(d)

def BinToOkc(s):
    d=''
    n=len(s)
    while n>=3:
        d=str(BintoDec(s[n-3:]))+d
        s=s[0:n-3]
        n=len(s)
    if len(s)>0:
        d=str(BintoDec(s))+d
    return(d)

def BinToHex(s):
    d=''
    ch=['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    n=len(s)
    while n>=4:
        d=ch[BintoDec(s[n-4:])-1]+d
        s=s[0:n-4]
        n=len(s)
    if len(s)>0:
        d=ch[BintoDec(s[n-4:])-1]+d
    return(d)
    
    
    
g='100001'
print(BintoDec(g))
print(BinToOkc(g))
print(BinToHex(g))
    
