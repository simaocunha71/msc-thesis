from functools import reduce
def square_nums(nums):
    new_list = []
    for i in nums:
        new_list.append(i ** 2)
    return new_list