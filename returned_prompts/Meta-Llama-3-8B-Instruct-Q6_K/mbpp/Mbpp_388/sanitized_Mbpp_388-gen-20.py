def highest_Power_of_2(n):
    if n <= 0:
        return 0
    power = 0
    while (1 << power) <= n:
        power += 1
    return (1 << (power - 1))