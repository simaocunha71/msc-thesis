def highest_Power_of_2(n):
    p = 0
    power_of_2 = 1
    while power_of_2 <= n:
        p = power_of_2
        power_of_2 *= 2
    return p