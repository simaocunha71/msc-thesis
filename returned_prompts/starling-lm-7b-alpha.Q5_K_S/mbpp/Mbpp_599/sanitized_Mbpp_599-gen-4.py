def sum_average(n):
    if(n<=0):
        return (0,0)
    else:
        s = (n*(n+1))//2
        return (s,s/n)