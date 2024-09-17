def eulerian_num(n, m):
    a = 0
    for i in range(n+1):
        if i == m:
            continue
        a += (n-i) * m**(n-i-1)
    return a