def power_base_sum(base, power):
    result = base ** power
    sum = 0
    while result > 0:
        sum += result % 10
        result //= 10
    return sum