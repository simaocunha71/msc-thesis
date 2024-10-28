def next_power_of_2(n):
    if n < 1:
        return 1
    power = 1
    while power < n:
        power *= 2
    return power