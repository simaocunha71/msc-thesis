import math
def is_nonagonal(n):
    return math.pow(n, 2) == sum(map(lambda x: x**2, range(1, n+1)))