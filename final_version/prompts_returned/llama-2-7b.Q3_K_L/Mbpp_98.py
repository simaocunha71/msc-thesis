"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

def multiply_num(nums):
    result = 0
    for value in nums:
        result += value * value
    return result / len(nums)
