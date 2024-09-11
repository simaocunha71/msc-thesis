def power_base_sum(base, power):
    result = pow(base, power)
    return sum(int(digit) for digit in str(result))  # convert the result to a string, iterate over each character (digit), convert back to int and sum them up