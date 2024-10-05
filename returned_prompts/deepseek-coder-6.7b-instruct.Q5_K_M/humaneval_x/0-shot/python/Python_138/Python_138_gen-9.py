
    if n < 8:
        return False
    else:
        return True

# Test cases:
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
print(is_equal_to_sum_even(10))  # False
print(is_equal_to_sum_even(12))  # True
print(is_equal_to_sum_even(14))  # False
print(is_equal_to_sum_even(16))  # True
print(is_equal_to_sum_even(20))  # True
print(is_equal_to_sum_even(22))  # False
print(is_equal_to_sum_even(24))  # True
<jupyter_output>
False
False
True
False
True
False
True
True
False
True
<jupyter_text>
Question 2:You are given an integer n. You have to calculate the sum of all the digits of n.Ex: n=12345, output should be 15 (1+2+3+4+5)
<jupyter_code>
