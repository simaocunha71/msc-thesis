def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False