def sumofFactors(n):
    sum=0
    i=1
    while i<=n:
        if(n%i==0):
            if(i%2==0):
                sum=sum+i
        i=i+1
    return sum