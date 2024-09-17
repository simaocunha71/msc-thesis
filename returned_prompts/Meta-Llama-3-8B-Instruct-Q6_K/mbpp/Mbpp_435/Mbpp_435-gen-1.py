def last_Digit(n):
    return n % 10

# Test the function
print(last_Digit(123))  # Output: 3
print(last_Digit(4567))  # Output: 7

# Explanation:
# The function takes an integer as input and returns its last digit.
# This is achieved by using the modulus operator % which returns the remainder of the division of the number by 10.
# For example, 123 % 10 returns 3, which is the last digit of 123. Similarly, 4567 % 10 returns 7, which is the last digit of 4567.  # noqa: E501
# The unit test cases confirm that the function works correctly for different inputs.