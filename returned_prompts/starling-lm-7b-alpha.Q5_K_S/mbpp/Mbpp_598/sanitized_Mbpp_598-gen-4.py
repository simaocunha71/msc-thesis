def armstrong_number(n):
    num=n
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem**3)
        num=num//10
    if(sum==n):
        return True
    else:
        return False