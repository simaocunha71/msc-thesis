def power_base_sum(base, power):
    result = 0
    for _ in range(power + 1):
        result += base
    return result