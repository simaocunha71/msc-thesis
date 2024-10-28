def next_Perfect_Square(n):
    i = int(n ** 0.5) + 1
    while True:
        i += 1
        square = i * i
        if square > n:
            return square