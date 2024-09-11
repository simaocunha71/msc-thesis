def is_nonagonal(n):
    return n % 7 == 0


def nth_nonagonal(n):
    return (n ** 3 + n) // 6


def test_nth_nonagonal():
    assert is_nonagonal(10) == True
    assert is_nonagonal(11) == False
    assert nth_nonagonal(0) == 0
    assert nth_nonagonal(1) == 1
    assert nth_nonagonal(2) == 4
    assert nth_nonagonal(3) == 9
    assert nth_nonagonal(4) == 20
    assert nth_nonagonal(5) == 43
    assert nth_nonagonal(6) == 86
    assert nth_nonagonal(7) == 149
    assert nth_nonagonal(8) == 238
    assert nth_nonagonal(9) == 355
    assert nth_nonagonal(10) == 325


test_nth_nonagonal()


def nth_nonagonal(n):
    return (n ** 3 + n) // 6


"""
Write a function to find the nth nonagonal number.
"""

# ANSWER
# Here's a step-by-step guide on how to solve this problem:

# Step 1: Understand the problem
# The problem asks us to write a function that can find the nth nonagonal number. A nonagonal number is a polygon with 7 sides.

# Step 2: Research the concept
# After understanding the problem, we need to research the concept of nonagonal numbers. A nonagonal number can be calculated using the formula (n^3 + n)/6.

# Step 3: Write the function
# Based on the formula, we can write the function nth_nonagonal(n) that takes an integer n as input and returns the nth nonagonal number using the formula.

# Step 4: Test the function
# To ensure that our function is working correctly, we can write a set of test cases using the test_nth_nonagonal() function. This function