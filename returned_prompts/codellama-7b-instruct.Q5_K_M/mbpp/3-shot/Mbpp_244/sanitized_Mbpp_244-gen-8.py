def next_Perfect_Square(n):
    n += 1
    n &= -n
    return n