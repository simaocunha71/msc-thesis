def next_Perfect_Square(n):
    i = n
    while True:
        sq = i ** 0.5
        if sq == int(sq):
            return i
        i += 1