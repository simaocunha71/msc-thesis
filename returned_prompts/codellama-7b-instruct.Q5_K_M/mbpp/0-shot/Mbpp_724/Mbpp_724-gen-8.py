def power_base_sum(base, power):
    result = 0
    for digit in str(base**power):
        result += int(digit)
    return result

