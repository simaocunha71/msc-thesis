def catalan_number(n):
    res = 1
    for i in range(1, n+1):
        res *= (2*i)
        res //= (i+1)
    return res