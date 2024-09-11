def power(a, b):
    return a ** b

# Test
print(power(3,4) == 81)


# Explanation:
# The function power() takes two parameters, 'a' and 'b'. The function returns the result of 'a' raised to the power of 'b'. The function uses the exponentiation operator (**). The assert statement checks if the function returns the correct result for the given inputs (3 and 4), which should be 81.

"""
The function power(a, b) calculates the value of 'a' raised to the power of 'b'. It uses the exponentiation operator (**). The assert statement checks if the function returns the correct result for the given inputs (3 and 4), which should be 81.

Here's an example of how to use the function:

power(3, 4)  # Returns 81

In this example, the function is called with the inputs 3 and 4. The function calculates 3 raised to the power of 4, which is 81.
"""

# Time Complexity: O(1)
# Space Complexity: O(1)

# Tags: #Basic Calculations

# Test Cases:
# Test Case 1
print(power(2, 3) == 8)
# Expected Output: True

# Test Case 2
print(power(5, 2) == 25)
# Expected Output: True

# Test Case 3
print(power(0, 3) == 0)
# Expected Output: True

# Test Case 4
print(power(7, 1) == 7)
# Expected Output: True

# Test Case 5
print(power(3, 0) == 1)
# Expected Output: True

# Test Case 6
print(power(1, 0) == 1)
# Expected Output: True

# Test Case 7
print(power(1, 1) == 1)
# Expected Output: True

# Test Case 8
print(power(0, 0) == 1)
# Expected Output: True

# Test Case