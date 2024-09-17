def catalan_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        c = [0] * (n + 1)
        c[0] = 1
        c[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                c[i] += c[j] * c[i-1-j]
        return c[n]