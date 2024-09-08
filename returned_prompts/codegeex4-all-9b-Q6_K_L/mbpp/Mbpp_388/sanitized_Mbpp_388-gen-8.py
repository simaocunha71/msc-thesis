def highest_Power_of_2(n):
    if n <= 0:
        return 0
    power = 1
    while power <= n:
        power *= 2
    return power // 2