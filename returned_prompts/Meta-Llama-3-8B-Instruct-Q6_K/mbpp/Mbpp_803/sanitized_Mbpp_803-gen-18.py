def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    for i in range(1, n + 1):
        if i * i == n:
            return True
    return False