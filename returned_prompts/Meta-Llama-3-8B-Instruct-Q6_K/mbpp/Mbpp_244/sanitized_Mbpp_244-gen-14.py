def next_Perfect_Square(n):
    i = 1
    while True:
        if i ** 2 > n:
            return i ** 2
        i += 1