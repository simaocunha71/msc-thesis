def next_Perfect_Square(n):
    i = n
    while True:
        if i % 2 == 0:
            i += 1
        else:
            i = (i + 1) // 2
        if i * i == (i ** 2):
            return i