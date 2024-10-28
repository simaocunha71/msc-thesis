def power_base_sum(base, power):
    result = 0
    base_power = base ** power
    for digit in str(base_power):
        result += int(digit)
    return result