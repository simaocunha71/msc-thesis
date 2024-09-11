def next_Perfect_Square(n):
    i = int(math.sqrt(n)) + 1
    while True:
        square = i * i
        if square > n:
            return square
        i += 1