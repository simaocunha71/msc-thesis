def is_woodall(n):
    if n < 10:
        return False
    digits = list(map(int, str(n)))
    product = 1
    for d in digits:
        if d != 0:
            product *= d
    return product == 1