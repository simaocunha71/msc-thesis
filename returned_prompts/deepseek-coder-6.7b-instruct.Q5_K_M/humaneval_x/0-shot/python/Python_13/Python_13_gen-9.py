

def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))

