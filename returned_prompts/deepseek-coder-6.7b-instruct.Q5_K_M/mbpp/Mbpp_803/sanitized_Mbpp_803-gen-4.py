def is_perfect_square(n):
    import math
    sqrt = math.sqrt(n)

    if sqrt == int(sqrt):
        return True
    else:
        return False