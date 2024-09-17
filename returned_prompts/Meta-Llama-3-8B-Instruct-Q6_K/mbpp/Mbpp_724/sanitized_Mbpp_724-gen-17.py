def power_base_sum(base, power):
    result = 0
    value = 1
    for _ in range(power):
        value = value * base
        for digit in str(value):
            result += int(digit)
    return result