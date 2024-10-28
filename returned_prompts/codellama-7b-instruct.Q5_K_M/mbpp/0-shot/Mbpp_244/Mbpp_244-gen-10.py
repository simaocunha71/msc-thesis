def next_Perfect_Square(num):
    i = int(num ** 0.5)
    while i ** 2 != num:
        i += 1
    return i ** 2
