

def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))
print(greatest_common_divisor(12, 15))
print(greatest_common_divisor(1024, 768))
print(greatest_common_divisor(60, 48))
print(greatest_common_divisor(81, 153))


Output:

1
5
3
4
12
13
'''


def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


print(greatest_common_divisor(3, 5))  # 1
print(greatest_common_divisor(25, 15))  # 5
print(greatest_common_divisor(12, 15))  # 3
print(greatest_common_divisor(1024, 768))  # 256
print(greatest_common_divisor(60, 48))  # 12
print(greatest_common_divisor(81, 153))  # 9

# -----------------------------------------------
# Code:


def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Tests:
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(12, 15) == 3
assert greatest_common_divisor(1024, 768) == 256
assert greatest_common_divisor