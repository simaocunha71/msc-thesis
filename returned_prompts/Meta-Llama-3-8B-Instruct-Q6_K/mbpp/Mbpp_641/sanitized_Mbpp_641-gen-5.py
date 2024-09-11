def is_nonagonal(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    return int(((9*n**2 - 9*n) // 2) + 1) if n % 9 != 0 else None