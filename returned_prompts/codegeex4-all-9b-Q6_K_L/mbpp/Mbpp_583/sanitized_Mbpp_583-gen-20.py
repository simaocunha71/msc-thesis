def catalan_number(n):
    c = [0]*(n+1)
    c[0] = 1
    for i in range(1, n+1):
        c[i] = 0
        for j in range(i):
            c[i] += c[j]*c[i-j-1]
    return c[n]