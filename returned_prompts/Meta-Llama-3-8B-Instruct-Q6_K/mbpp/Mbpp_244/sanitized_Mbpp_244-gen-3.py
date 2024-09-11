def next_Perfect_Square(n):
    i = int(n**0.5) + 1
    while (i * i) > n:
        i -= 1
    return i * i + 1