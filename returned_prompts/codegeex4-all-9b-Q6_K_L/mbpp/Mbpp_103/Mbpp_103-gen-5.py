def eulerian_num(n, m):
    import math
    return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))


