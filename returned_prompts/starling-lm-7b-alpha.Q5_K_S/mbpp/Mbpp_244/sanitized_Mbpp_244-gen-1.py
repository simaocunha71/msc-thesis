from math import sqrt, ceil
def next_Perfect_Square(n):
    while True:
        if int(ceil(sqrt(n)))**2 == n+1:
            return n+1
        n += 1