def next_Perfect_Square(n):
    i = n
    while True:
        i += 1
        sqrt = int(i ** 0.5)
        if sqrt * sqrt == i:
            return i