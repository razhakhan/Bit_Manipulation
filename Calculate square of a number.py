def calculateSquare(n):
    n=abs(n)
    temp=n
    res=0
    pos=0
    while(temp):
        if(temp & 1):
            res+=(n<<pos)
        pos+=1
        temp=temp>>1
    return res

'''

n^2 = n * n
    n * (10101)
    n * (2^4+2^2+2^0)
    n * 2^4 + n * 2^2+ n * 2^0
    n<<4 + n <<2 + n<<0
    
'''
