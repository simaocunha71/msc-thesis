def catalan_number(n):
    fact = [1 for i in range(n+1)]
    for i in range(2, n+1):
        fact[i] = fact[i-1] * i

    res = fact[n] // (fact[n//2+1] * fact[n//2])
    return res