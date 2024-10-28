

def greatest_common_divisor(a: int, b: int) -> int:
    if a < b:
        return greatest_common_divisor(b, a)
    if a % b == 0:
        return b
    return greatest_common_divisor(b, a % b)


