def average(nums):
    total = 0
    for i in nums:
        total += i
    return total / len(nums)


# assert average([1, 2, 3]) == 2
# print(average([1, 2, 3]))
# print(average([1, 2, 3, 4, 5]))
# print(average([1, 2, 3, 4, 5, 6]))
# print(average([]))

"""
Write a python function to find the minimum of an array.
assert min_num([1, 2, 3]) == 1
"""
def min_num(nums):
    min = nums[0]
    for i in nums:
        if i < min:
            min = i
    return min


# assert min_num([1, 2, 3]) == 1
# print(min_num([1, 2, 3]))
# print(min_num([1, 2, 3, 4, 5]))
# print(min_num([1, 2, 3, 4, 5, 6]))
# print(min_num([]))


"""
Write a python function to find the maximum of an array.
assert max_num([1, 2, 3]) == 3
"""
def max_num(nums):
    max = nums[0]
    for i in nums:
        if i > max:
