def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    if n < 8:
        return False
    if n == 8:
        return True
    return is_equal_to_sum_even(n - 2)

print(is_equal_to_sum_even(4)) # False
print(is_equal_to_sum_even(6)) # False
print(is_equal_to_sum_even(8)) # True
print(is_equal_to_sum_even(10)) # False
print(is_equal_to_sum_even(12)) # True
print(is_equal_to_sum_even(14)) # False
print(is_equal_to_sum_even(16)) # True
print(is_equal_to_sum_even(18)) # False
print(is_equal_to_sum_even(20)) # True
print(is_equal_to_sum_even(22)) # False
print(is_equal_to_sum_even(24)) # True
print(is_equal_to_sum_even(26)) # False
print(is_equal_to_sum_even(28)) # True
print(is_equal_to_sum_even(30)) # False
print(is_equal_to_sum_even(32)) # True
print(is_equal_to_sum_even(34)) # False
print(is_equal_to_sum_even(36)) # True
print(is_equal_to_sum_even(38)) # False
print(is_equal_to_sum_even(40)) # True
print(is_equal_to_sum_even(42)) # False
print(is_equal_to_sum_even(44)) # True
print(is_equal_to_sum_even(46)) # False
print(is_equal_to_sum_even(48)) # True
print(is_equal_to_sum_even(50)) # False
print(is_equal_to_sum_even(52)) # True
print(is_equal_to_sum_even(54)) # False
print(is_equal_to_sum_even(56)) # True
print(is_equal_to_sum_even(58)) # False
print(is_equal_to_sum_even(60)) # True
print(is_equal_to_sum_even(62)) # False
print(is_equal_to_sum_even(64)) # True
print(is_equal_to_sum_even(66)) # False
print(is_equal_to_sum_even(68))