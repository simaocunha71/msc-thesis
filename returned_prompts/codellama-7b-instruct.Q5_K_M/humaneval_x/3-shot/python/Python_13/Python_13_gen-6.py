    if a % b == 0:
        return b
    return greatest_common_divisor(b, a % b)


