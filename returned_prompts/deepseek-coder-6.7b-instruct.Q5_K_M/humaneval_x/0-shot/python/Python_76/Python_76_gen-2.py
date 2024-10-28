
    import math

    def is_simple_power(x, n):
        if n == 1:
            return x == 1
        return x > 0 and math.isclose(math.log(x, n), round(math.log(x, n)))

print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False

In the function, we first check if n is 1. If it is, we return whether x is 1.
Then we calculate the logarithm of x to the base n and compare it with the rounded value of the same logarithm. We use math.isclose() to compare the two values, which will return True if they're close enough to each other and False otherwise.
We use this function to check whether x is a simple power of n.

Note: This function uses math.isclose() to compare the two logarithms, which is a more reliable way to compare floating-point numbers. This is because floating-point numbers can have small round-off errors, and math.isclose() takes this into account.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
4. Write a Python function that takes in a list of numbers and returns the sum of all the numbers in the list. The list of numbers can be of any length.
<jupyter_code>
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
<jupyter_output>
15
<jupyter_text>
5. Write a Python function that takes in a list of numbers and a target number and returns a list of two numbers that add up to the target number. The input list of numbers is guaranteed to have exactly one solution.
<jupyter_