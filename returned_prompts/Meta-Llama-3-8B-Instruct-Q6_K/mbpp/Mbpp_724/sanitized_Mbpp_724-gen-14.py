def power_base_sum(base, power):
    result = 1
    for _ in range(power):
        result *= base
    return sum(int(digit) for digit in str(result))