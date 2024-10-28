def power_base_sum(base, power):
    result = 0
    for digit in str(base ** power):
        result += int(digit)
    return result
    # Alternative solution
    # return sum(int(digit) for digit in str(base ** power))  # python 3.5+
    # return sum(map(int, str(base ** power)))  # python 3.5+