def highest_Power_of_2(n):
    p = 0
    while n > 0:
        n >>= 1
        p += 1
    return (1 << p) - 1