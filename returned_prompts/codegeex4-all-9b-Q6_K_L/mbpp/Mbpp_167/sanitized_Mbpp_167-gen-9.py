def next_power_of_2(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    power = 1
    while power < n:
        power *= 2
    return power