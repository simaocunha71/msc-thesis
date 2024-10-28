def is_polite(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n + is_polite(n-1)