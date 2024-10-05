def is_equal_to_sum_even(n):
    if n % 2 == 0 and n >= 8:
        return True
    else:
        return False

print(is_equal_to_sum_even(4)) # False
print(is_equal_to_sum_even(6)) # False
print(is_equal_to_sum_even(8)) # True