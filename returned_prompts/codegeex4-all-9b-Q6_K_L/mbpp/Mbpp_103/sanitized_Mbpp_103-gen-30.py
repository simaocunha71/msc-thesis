def eulerian_num(n, m):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact // (m ** (n - m) * (n - m) ** m)