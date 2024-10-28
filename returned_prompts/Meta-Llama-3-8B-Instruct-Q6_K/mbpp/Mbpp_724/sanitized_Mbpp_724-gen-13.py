def power_base_sum(base, power):
    if not isinstance(base, int) or base <= 0:
        raise ValueError("Base must be a positive integer")
    if not isinstance(power, int) or power < 0:
        raise ValueError("Power must be a non-negative integer")
    result = 0
    for digit in str(base ** power):
        result += int(digit)
    return result