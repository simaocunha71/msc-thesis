def is_polite(n: int) -> bool:
    return n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n))+1))

