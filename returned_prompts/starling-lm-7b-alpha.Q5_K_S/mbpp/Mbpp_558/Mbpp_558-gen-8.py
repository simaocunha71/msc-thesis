def digit_distance_nums(n1,n2):
    n1 = str(n1)
    n2 = str(n2)
    if len(n1) < len(n2):
        n1 = '0' * (len(n2) - len(n1)) + n1
    elif len(n1) > len(n2):
        n2 = '0' * (len(n1) - len(n2)) + n2
    s = 0
    for i in range(len(n1)):
        s += abs(int(n1[i]) - int(n2[i]))
    return s

# Test
print(digit_distance_nums(1, 2))
print(digit_distance_nums(135, 153))

"""
Explanation:

The key point is to make sure that both integers have the same number of digits.
If one is shorter than the other, we pad the shorter one with zeroes until they have the same number of digits.
Then, we iterate through each digit of the padded numbers and calculate the absolute difference between the digits.
Finally, we sum all these absolute differences to obtain the result.
"""

# Time Complexity: O(n), where n is the maximum number of digits between the two numbers.
# Space Complexity: O(1), we don't use any extra space.

# This solution can handle very large numbers as long as the number of digits is not too long (e.g. less than 10^18).
# For numbers with more than 10^18 digits, we will need to use a different approach.

# Note: Python's int is a signed integer, so when we subtract a larger number from a smaller number, we will get a negative result.
# In this case, we take the absolute value of the difference to ensure the result is non-negative.
"""

"""

# Time Complexity: O(n)
# Space Complexity: O(1)

"""

"""

"""

"""

"""

```
```