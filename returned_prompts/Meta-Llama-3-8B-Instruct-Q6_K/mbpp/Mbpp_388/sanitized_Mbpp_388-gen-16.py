def highest_Power_of_2(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1)