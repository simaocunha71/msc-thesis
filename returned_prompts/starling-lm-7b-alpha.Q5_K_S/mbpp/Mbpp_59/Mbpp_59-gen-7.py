def is_octagonal(n):
    return (n % 8 == 0) or (n % 8 == 1)

def nth_octagonal(n):
    return 8 * (n ** 2) - (8 * n) - 1

def test_is_octagonal():
    assert is_octagonal(5) == True

def test_nth_octagonal():
    assert nth_octagonal(5) == 65

test_is_octagonal()
test_nth_octagonal()

"""
The octagonal numbers are a sequence of numbers in which each number is the sum of the previous two octagonal numbers and the previous two non-octagonal numbers, starting with 1 and 9.
"""

# Here are the first few octagonal numbers:
# 1, 9, 21, 45, 73, 109, 153, 211, 285, 373, 475, 591, 721, 873, 1049, 1241, ...

# The nth octagonal number can be calculated using the formula:
# nth_octagonal(n) = 8 * (n ** 2) - (8 * n) - 1

# Here's a function to determine if a given number is an octagonal number:

"""
def is_octagonal(n):
    return (n % 8 == 0) or (n % 8 == 1)
"""

# Here's a function to calculate the nth octagonal number:

"""
def nth_octagonal(n):
    return 8 * (n ** 2) - (8 * n) - 1
"""

# Here are some tests for the functions:

"""
def test_is_octagonal():
    assert is_octagonal(5) == True
"""

"""
def test_nth_octagonal():
    assert nth_octagonal(5) == 65
"""

# test_is_octagonal()
# test_nth_octagonal()

"""
The oct