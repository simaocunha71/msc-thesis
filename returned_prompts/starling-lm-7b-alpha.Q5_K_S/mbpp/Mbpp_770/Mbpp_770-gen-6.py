"""
To find the sum of fourth power of first n odd natural numbers you can follow the below approach:

1. Create a function odd_num_sum that takes one argument n.
2. Initialize a variable sum with 0. This variable will hold the final result.
3. Use a for loop to iterate from 1 to 2n. Increment by 2 in each iteration so as to get only odd natural numbers.
4. In each iteration, calculate the fourth power of the number using the exponent operator ** and add it to the sum.
5. Once the loop is complete, return the value of sum.
6. Define a test case to verify the correctness of the function.

Here is the Python code to implement the above approach:
"""

def odd_num_sum(n):
    """ Find the sum of the fourth powers of the first n odd natural numbers."""
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i ** 4
    return sum

# Testing the function
assert odd_num_sum(2) == 82

# This code is contributed by Ankit Rajpurohit (coderbyborne)

"""
The above Python code defines a function odd_num_sum that calculates the sum of fourth powers of the first n odd natural numbers. The function uses a for loop to iterate through the odd numbers from 1 to 2n (exclusive) and adds the fourth power of each number to the sum. The function returns the final sum.

The provided test case asserts that when the function is called with the argument 2, it should return 82. This test case verifies the correctness of the function implementation.
"""


# Python3 program to find sum of first n odd
# natural numbers' fourth powers

# Function to find sum of first n odd
# natural numbers' fourth powers
def odd_num_sum(n):
    # Initialize result
    sum = 0

    # Consider all odd numbers from 1 to 2n - 1
    for i in range(1, 2 * n, 2):
        # Add i^4 to sum
        sum += i ** 4

    # Return the sum
    return sum
