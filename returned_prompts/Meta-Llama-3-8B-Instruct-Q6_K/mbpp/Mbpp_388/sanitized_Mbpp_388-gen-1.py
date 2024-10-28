def highest_Power_of_2(n):
    if n < 1:
        return 0
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1) if power > 1 else 0