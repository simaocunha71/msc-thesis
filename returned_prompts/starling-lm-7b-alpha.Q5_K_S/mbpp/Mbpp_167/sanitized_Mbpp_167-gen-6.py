import math
def next_power_of_2(n):
    p = 0
    while n > 0:
        p += 1
        n >>= 1
    return 1 << p