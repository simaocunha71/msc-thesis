def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n