def power_base_sum(base: int, power: int) -> int:
    if power == 0:
        return 1
    else:
        return base + power_base_sum(base, power - 1)