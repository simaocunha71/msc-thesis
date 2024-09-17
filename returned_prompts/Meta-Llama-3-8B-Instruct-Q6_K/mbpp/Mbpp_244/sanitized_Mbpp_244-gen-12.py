def next_Perfect_Square(n):
    i = 1
    while True:
        if i * i > n:
            return i * i
        i += 1