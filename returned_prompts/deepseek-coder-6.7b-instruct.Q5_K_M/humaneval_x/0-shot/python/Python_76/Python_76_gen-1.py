
def is_simple_power(x, n):
    if n == 1:
        return x == 1
    while x > 1:
        x /= n
    return x == 1


print(is_simple_power(1, 4))  # => true
print(is_simple_power(2, 2))  # => true
print(is_simple_power(8, 2))  # => true
print(is_simple_power(3, 2))  # => false
print(is_simple_power(3, 1))  # => false
print(is_simple_power(5, 3))  # => false

# The above function works by dividing x by n continuously until x is no longer divisible.
# If x is 1 at this point, then n is a simple power of x. If x is not 1, then n is not a simple power of x.

# Note: This solution assumes that x and n are non-negative integers. If x and/or n can be negative or non-integer, then the solution will need to be adapted accordingly.

# Also note that this solution has a time complexity of O(log x), as it performs a division operation for each power of n that divides x.

# Finally, this solution does not consider 0 as a power of any number, as per the mathematical definition of the operation. If 0 is considered a power of any number, then the solution will need to be adapted accordingly.
<jupyter_output>
True
True
True
False
False
False
<jupyter_text>
Problem 3: You are given two arrays of integers. Write a function that returns an array of integers that contains all the values that exist in both arrays. The function should return an empty array if there are no common values.The function should be able to handle negative numbers and zeros.
<jupyter_code>
def common_elements(arr1, arr2):
    """Your task is to write a function that takes in two arrays of integers,
    and returns an array of integers containing the common elements in the arrays.
    If there are no common elements, the function should return an empty array.
    The function should be able to handle negative numbers