def power_base_sum(base, power):
    total = 0
    num = base ** power
    while num > 0:
        total += num % 10
        num //= 10
    return total