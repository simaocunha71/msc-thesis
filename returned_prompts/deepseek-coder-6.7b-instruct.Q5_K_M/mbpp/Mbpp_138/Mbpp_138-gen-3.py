def is_Sum_Of_Powers_Of_Two(n):
    if n < 1:
        return False
    while n % 2:
        n /= 2
    return n > 0

print(is_Sum_Of_Powers_Of_Two(10))

# Output: True

# This is because 10 = 2^3 + 2^1, and both 2^3 and 2^1 are non-zero powers of 2.

# The function works by repeatedly dividing the number by 2 until it becomes an even number. If the number becomes 1 or more than 1 at the end of this process, it means the number can be represented as the sum of non-zero powers of 2. If not, it means the number cannot be represented as the sum of non-zero powers of 2.

# In the example given, 10 is an even number, so the function returns True.
<jupyter_output>
True
<jupyter_text>
Question 4
<jupyter_code>
