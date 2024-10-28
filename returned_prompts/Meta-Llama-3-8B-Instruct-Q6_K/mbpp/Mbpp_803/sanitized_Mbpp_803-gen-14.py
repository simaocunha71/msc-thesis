def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    sqrt = int(n**0.5)
    return sqrt * sqrt == n