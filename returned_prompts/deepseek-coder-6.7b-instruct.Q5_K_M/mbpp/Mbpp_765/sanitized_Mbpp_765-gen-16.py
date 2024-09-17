def is_polite(n):
    p=[0]*(n+1)
    c=0
    for i in range(1,n+1):
        if (i%2)!=0:
            p[i]=p[i-1]+pow(2,c)
            c+=1
        else:
            p[i]=p[i-1]
    return p[n]