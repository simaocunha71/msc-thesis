def is_equal_to_sum_even(n):
    if n < 8 or n % 2 != 0:
        return False
    for i in range(2, n, 2):
        if n - i >= 8:
            return True
    return False

print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
print(is_equal_to_sum_even(10))  # True
print(is_equal_to_sum_even(12))  # True