def catalan_number(n):
    if n==0:
        return 1
    else:
        return (4*catalan_number(n-1))/(n+1)