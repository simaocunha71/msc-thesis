def armstrong_number(num):
    temp=num
    sum=0
    n=len(str(num))
    while temp>0:
        r=temp%10
        sum=sum+r**n
        temp=temp//10
    return sum==num