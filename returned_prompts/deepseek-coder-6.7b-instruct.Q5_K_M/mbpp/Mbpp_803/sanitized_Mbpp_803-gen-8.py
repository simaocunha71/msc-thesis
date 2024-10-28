def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    x = n // 2
    seen = {x}
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True