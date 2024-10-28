def power_base_sum(base, power):
    result = pow(base, power)
    sum_digits = sum(int(digit) for digit in str(result))
    return sum_digits