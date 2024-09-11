def next_Perfect_Square(n):
    i = int(n**0.5) + 1
    while (i + 1) ** 2 <= n:
        i += 1
    return i ** 2