def power_base_sum(base: int, power: int) -> int:
    power_base = base ** power
    return sum(int(digit) for digit in str(power_base))


