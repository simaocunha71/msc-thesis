def next_Perfect_Square(n):
    x = int(n**0.5)
    while True:
        y = x*x
        if y > n:
            return y
        x += 1