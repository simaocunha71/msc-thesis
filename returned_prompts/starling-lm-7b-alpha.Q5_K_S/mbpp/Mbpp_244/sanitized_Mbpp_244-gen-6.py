from math import ceil, sqrt
def next_Perfect_Square(x):
    sq = int(ceil(sqrt(x)))
    while True:
        if sq*sq == x:
            return sq*sq
        else:
            sq += 1