
    if n % 2 != 0:
        return False
    else:
        return True

# Test cases
print(is_equal_to_sum_even(4)) # False
print(is_equal_to_sum_even(6)) # False
print(is_equal_to_sum_even(8)) # True
print(is_equal_to_sum_even(10)) # False
print(is_equal_to_sum_even(12)) # True

# Test case with a large number
print(is_equal_to_sum_even(10000)) # False
<jupyter_output>
False
False
True
False
True
False
<jupyter_text>
Problem 4: Write a Python function that accepts a list of numbers and returns the sum of all the numbers in the list.
<jupyter_code>
