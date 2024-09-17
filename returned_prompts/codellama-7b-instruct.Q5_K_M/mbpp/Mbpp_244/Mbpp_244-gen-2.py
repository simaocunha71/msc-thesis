
def next_Perfect_Square(n):
    n = n + 1
    n = n & (~(n - 1))
    return n


