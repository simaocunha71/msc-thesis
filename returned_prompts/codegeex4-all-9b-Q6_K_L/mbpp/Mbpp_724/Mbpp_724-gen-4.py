def power_base_sum(base: int, power: int) -> int:
    result = base ** power
    return sum(int(digit) for digit in str(result))

