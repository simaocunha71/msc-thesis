def next_Perfect_Square(n):
    i = n
    while True:
        if i**0.5 % 1 == 0:
            return int(i)
        i += 1
    return None
    # Alternative solution
    # return int((n + 1) ** 0.5) ** 2