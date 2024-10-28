def eulerian_num(n: int, m: int) -> int:
    return math.factorial(n) / (math.factorial(n - m) * math.factorial(m))

