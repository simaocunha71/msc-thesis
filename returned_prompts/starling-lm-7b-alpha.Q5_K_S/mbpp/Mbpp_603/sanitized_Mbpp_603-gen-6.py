def get_ludic(n):
    res = []
    for i in range(1,n+1):
        j = i
        while j <= n:
            if j % i == 0:
                res.append(i)
            j += i
    return res