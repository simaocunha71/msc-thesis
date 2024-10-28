def highest_Power_of_2(n):
    if n == 0:
        return 0
    power = 0
    while n > 0:
        n >>= 1
        power += 1
    return 2 ** (power - 1)
