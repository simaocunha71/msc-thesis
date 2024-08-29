def power_base(base, power):
    return base ** power
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
def power_base_sum(base, power):
    return sum_digits(power_base(base, power))