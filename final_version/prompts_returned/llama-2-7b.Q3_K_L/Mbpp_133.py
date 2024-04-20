"""
Write a function to calculate the sum of the negative numbers of a given list of numbers.
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
"""

def sum_negativenum(nums):
    res = 0 #initilize the result variable

    for i in range(len(nums)):
        if nums[i] < 0:
            res -= nums[i]

    return res