def is_simple_power(x, n):
    if n == 1:
        return True
    if x < 1:
        return False
    if x % n != 0:
        return False
    root = int(x ** (1.0 / n))
    return root ** n == x
    



# test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
print(is_simple_power(27, 3))  # True
print(is_simple_power(64, 4))  # True
print(is_simple_power(25, 5))  # True
print(is_simple_power(36, 4))  # True
print(is_simple_power(16, 4))  # True
print(is_simple_power(81, 3))  # True
print(is_simple_power(9, 3))  # True
print(is_simple_power(10, 2))  # False
print(is_simple_power(12, 3))  # False
print(is_simple_power(13, 2))  # False
print(is_simple_power(14, 2))  # False
print(is_simple_power(15, 3))  # False
print(is_simple_power(16, 2))  # True
print(is_simple_power(20, 4))  # False
print(is_simple_power(21, 3))  # False
print(is_simple_power(22, 2))  # False
print(is_simple_power(23, 3))  # False
print(is_simple_power(24, 3))  # False
print(is_simple_power(25, 2))  # False
print(is_simple_power(26, 2))  # False
print(is_simple_power(27, 3))  # True
print(is_simple_power(28, 2))  # False
print(is_simple_power(29, 2))  # False
print(is_simple_power(30, 3))  # False
print(is_simple_power(31, 2))  # False
print(is_simple_power(32, 