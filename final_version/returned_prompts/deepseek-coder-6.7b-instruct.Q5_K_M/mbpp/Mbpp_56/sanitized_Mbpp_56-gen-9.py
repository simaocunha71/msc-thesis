def check(n):
    rev = int(str(n)[::-1])
    twice_rev = 2 * rev
    return twice_rev - 1 == n