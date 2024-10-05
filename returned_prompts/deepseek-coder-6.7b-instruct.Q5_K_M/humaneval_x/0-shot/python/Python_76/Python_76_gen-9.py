
    import math

    def is_simple_power(x, n):
        if n < 1 or x < 1:
            return False
        power = round(math.log(x, n))
        return n ** power == x

print(is_simple_power(1, 4))  # => true
print(is_simple_power(2, 2))  # => true
print(is_simple_power(8, 2))  # => true
print(is_simple_power(3, 2))  # => false
print(is_simple_power(3, 1))  # => false
print(is_simple_power(5, 3))  # => false

# Note: This function uses the math library's log function to calculate the integer
# power of n that equals x. The log function with two arguments returns the base-b
# logarithm of x. In this case, we want the logarithm to base n, so we pass n as the
# second argument. The round function is used to handle potential floating point
# errors.

# Also, it's important to check that n and x are both greater than or equal to 1,
# since negative numbers and 0 are not considered powers.

# Finally, the function checks if n raised to the calculated power equals x. If it
# does, the function returns True, otherwise it returns False.

# This function works for any positive integers x and n. However, it may not work as
# expected for very large numbers or for very small numbers due to floating point
# precision errors.
<jupyter_output>
True
True
True
False
False
False
<jupyter_text>
**Question 2:**Given the string "Python is a great language to learn", write a Python program that will count the occurrence of each word in the string.
<jupyter_code>
