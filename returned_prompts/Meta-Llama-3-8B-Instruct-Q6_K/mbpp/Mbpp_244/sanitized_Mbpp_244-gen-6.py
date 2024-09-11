def next_Perfect_Square(n):
    i = n + 1
    while True:
        sqrt = int(i ** 0.5)
        if sqrt * sqrt == i:
            return i
        i += 1