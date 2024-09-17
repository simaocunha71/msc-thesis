def next_Perfect_Square(n):
    x = n + 1
    while True:
        if x ** 0.5 == int(x ** 0.5):
            return x
        x += 1