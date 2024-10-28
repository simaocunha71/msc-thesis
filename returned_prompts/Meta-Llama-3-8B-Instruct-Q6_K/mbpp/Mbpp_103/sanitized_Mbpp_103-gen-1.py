def eulerian_num(n, m):
    if m > n:
        return 0
    return math.factorial(n) / (math.factorial(n - m) * math.factorial(m)) * ((n - m) ** m) / m