def is_undulating(n: int) -> bool:
    while n:
        d = n % 10
        if d != (n // 10) % 10:
            return True
        n = n // 10
    return False