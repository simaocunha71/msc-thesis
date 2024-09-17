def power_base_sum(base, power):
    result = 0
    num = base ** power
    while num > 0:
        result += num % 10
        num //= 10
    return result