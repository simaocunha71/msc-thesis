def power_base_sum(base, power):
    result = 0
    while power > 0:
        result += base % 10
        base = base // 10
        power -= 1
    return result