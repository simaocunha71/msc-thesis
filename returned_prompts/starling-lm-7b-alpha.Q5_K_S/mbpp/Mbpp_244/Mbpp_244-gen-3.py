
def next_Perfect_Square(n):
    i = n
    while True:
        if i ** 2 > n:
            i += 1
        else:
            return i ** 2


