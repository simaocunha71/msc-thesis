def is_simple_power(x, n):
    if x == 1:
        return True
    for i in range(2, int(x**0.5) + 1):
        if x % (n**i) == 0:
            return False
    return True
# Test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
print(is_simple_power(4, 2))  # True
print(is_simple_power(9, 3))  # True
print(is_simple_power(27, 3))  # True
print(is_simple_power(125, 5))  # True
print(is_simple_power(16, 2))  # True
print(is_simple_power(25, 5))  # True
print(is_simple_power(36, 4))  # True
print(is_simple_power(64, 4))  # True
print(is_simple_power(81, 3))  # True
print(is_simple_power(100, 4))  # True
print(is_simple_power(121, 11))  # True
print(is_simple_power(144, 6))  # True
print(is_simple_power(169, 13))  # True
print(is_simple_power(196, 7))  # True
print(is_simple_power(225, 5))  # True
print(is_simple_power(256, 4))  # True
print(is_simple_power(289, 17))  # True
print(is_simple_power(324, 6))  # True
print(is_simple_power(361, 19))  # True
print(is_simple_power(400, 8))  # True
print(is_simple_power(441, 7))  # True
print(is_simple_power(484, 11))  # True
print(is_simple_power(529, 23))  # True
print(is_simple_power(576, 8))  # True
print(is_simple_power(625, 5))  # True
print(is_simple_power(676, 13))  # True
print