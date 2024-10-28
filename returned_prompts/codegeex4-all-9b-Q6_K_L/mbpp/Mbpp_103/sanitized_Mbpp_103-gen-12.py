def eulerian_num(n: int, m: int) -> int:
    if n < 0 or m < 0:
        return -1
    return math.factorial(n+m) // (math.factorial(n) * math.factorial(m))