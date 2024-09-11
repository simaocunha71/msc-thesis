def square_nums(nums):
    new_list = []
    for i in nums:
        new_list.append(i ** 2)
    return new_list

def test_square_nums():
    assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

test_square_nums()

# Using List comprehension
def square_nums_list(nums):
    return [i ** 2 for i in nums]

def test_square_nums_list():
    assert square_nums_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

test_square_nums_list()

# Using Map
def square_nums_map(nums):
    return list(map(lambda x: x ** 2, nums))

def test_square_nums_map():
    assert square_nums_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

test_square_nums_map()

# Using reduce
from functools import reduce
def square_nums_reduce(nums):
    return reduce(lambda x, y: x + y ** 2, nums)

def test_square_nums_reduce():
    assert square_nums_reduce([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385