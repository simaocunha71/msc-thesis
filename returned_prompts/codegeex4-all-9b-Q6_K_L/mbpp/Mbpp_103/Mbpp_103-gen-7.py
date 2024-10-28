def eulerian_num(n, m):
    fact = [1]
    for i in range(1, n+1):
        fact.append(fact[-1]*i)
    return fact[n+m-2]//(fact[n-1]*fact[m])

