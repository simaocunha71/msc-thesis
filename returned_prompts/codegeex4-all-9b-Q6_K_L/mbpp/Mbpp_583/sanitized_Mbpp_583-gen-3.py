def catalan_number(n):
    if n <= 1:
        return 1
    res = [0 for _ in range(n+1)]
    res[0] = 1
    for i in range(1, n+1):
        res[i] = 0
        for j in range(i):
            res[i] += res[j] * res[i-1-j]
    return res[n]