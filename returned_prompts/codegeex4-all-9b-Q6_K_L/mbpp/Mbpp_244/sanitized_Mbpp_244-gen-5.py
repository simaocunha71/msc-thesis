def next_Perfect_Square(n):
    while True:
        n += 1
        if int(n**0.5)**2 == n:
            return n