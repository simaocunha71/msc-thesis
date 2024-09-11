"""
You can achieve this by creating a function that takes a list of numbers as an argument and uses a list comprehension to calculate the cube of each number. Here's an example implementation:

def cube_nums(nums):
    """Return a list of the cubes of the numbers in `nums`."""
    return [num ** 3 for num in nums]

To test the function, you can use the `assert` statement to verify the output of the `cube_nums` function against the expected result. Here's an example test case:

def test_cube_nums():
    assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    print("All tests passed.")

test_cube_nums()
"""

from collections import Counter

def cube_nums(nums):
    """Return a list of the cubes of the numbers in `nums`."""
    return [num ** 3 for num in nums]

def test_cube_nums():
    assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    print("All tests passed.")

test_cube_nums()


# Another Solution
def cube_nums(nums):
    return [n**3 for n in nums]
```
t_cube_nums = [cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
assert t_cube_nums == [1, 8, 27, 6