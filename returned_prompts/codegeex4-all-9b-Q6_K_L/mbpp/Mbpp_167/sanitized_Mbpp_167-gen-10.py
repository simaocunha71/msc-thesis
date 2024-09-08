def next_power_of_2(n: int) -> int:
    if n == 0:
        return 1
    power = 1
    while power < n:
        power <<= 1
    return power