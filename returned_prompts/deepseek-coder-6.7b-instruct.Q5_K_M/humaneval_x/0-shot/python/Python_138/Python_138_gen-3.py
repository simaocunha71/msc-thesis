
    if n < 8:
        return False
    else:
        return True

print(is_equal_to_sum_even(4)) # False
print(is_equal_to_sum_even(6)) # False
print(is_equal_to_sum_even(8)) # True

# The function is_equal_to_sum_even(n) checks if the given number n can be written as the sum of exactly 4 positive even numbers. 
# In this case, it's only necessary to check if n is greater or equal to 8, because 4 positive even numbers (2, 2, 2, 2) will always sum up to 8 or greater.
# Therefore, if n is greater or equal to 8, the function returns True; otherwise it returns False.
<jupyter_output>
False
False
True
<jupyter_text>
Question 3: Write a Python function that takes a string and returns the number of vowels in it.
<jupyter_code>
