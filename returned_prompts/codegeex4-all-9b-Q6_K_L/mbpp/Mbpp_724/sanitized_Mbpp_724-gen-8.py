def power_base_sum(base, power):
    total = 0
    base_power = base ** power
    while base_power > 0:
        total += base_power % 10
        base_power //= 10
    return total