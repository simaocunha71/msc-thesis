def catalan_number(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        cn = [0]*(n+1)
        cn[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                cn[i] += cn[j]*cn[i-1-j]
        return cn[n]