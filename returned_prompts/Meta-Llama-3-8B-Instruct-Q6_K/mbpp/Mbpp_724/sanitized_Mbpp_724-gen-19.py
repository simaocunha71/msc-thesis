def power_base_sum(base, power):
    result = 0
    for i in range(power):
        result += sum(int(digit) for digit in str(base ** i))
    return result