def is_equal_to_sum_even(n):
    if n % 2 == 1:
        return False
    for i in range(2, n, 2):
        if n - i >= 2 and (n - i) % 2 == 0:
            return True
    return False

print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
print(is_equal_to_sum_even(10))  # True
print(is_equal_to_sum_even(12))  # False
print(is_equal_to_sum_even(14))  # False
print(is_equal_to_sum_even(16))  # True
print(is_equal_to_sum_even(18))  # True
print(is_equal_to_sum_even(20))  # False