def next_Perfect_Square(n):
    i = int(n ** 0.5) + 1
    while True:
        square = i ** 2
        if square > n:
            return square
        i += 1