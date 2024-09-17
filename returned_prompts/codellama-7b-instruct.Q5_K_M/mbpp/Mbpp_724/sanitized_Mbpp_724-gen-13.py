def power_base_sum(base, power):
    sum = 0
    for digit in str(base ** power):
        sum += int(digit)
    return sum