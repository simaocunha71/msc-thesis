def next_Perfect_Square(n):
    if n < 0:
        return None
    i = int(n**0.5) + 1
    return i**2