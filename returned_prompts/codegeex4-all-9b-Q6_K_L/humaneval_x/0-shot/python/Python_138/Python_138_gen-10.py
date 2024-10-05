def is_equal_to_sum_even(n):
    return n % 8 == 0

# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
print(is_equal_to_sum_even(12))  # True
print(is_equal_to_sum_even(16))  # True
print(is_equal_to_sum_even(20))  # False