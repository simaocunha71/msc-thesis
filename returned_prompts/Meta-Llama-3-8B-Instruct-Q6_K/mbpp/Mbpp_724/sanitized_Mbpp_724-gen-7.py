def power_base_sum(base, power):
    result = pow(base, power)
    return sum(int(digit) for digit in str(result))