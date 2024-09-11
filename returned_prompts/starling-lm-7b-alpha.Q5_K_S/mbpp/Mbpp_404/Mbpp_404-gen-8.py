minimum = lambda a,b: a if a < b else b

assert minimum(1,2) == 1




























"""
Created on Thu Sep 29 12:14:49 2016

@author: vivek
"""

def minimum(a,b):
    if a<b:
        return a
    else:
        return b

def maximum(a,b):
    if a>b:
        return a
    else:
        return b

def sum_of_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

def multiply_list(nums):
    total = 1
    for num in nums:
        total *= num
    return total

def find_max_product(nums):
    return max(multiply_list(nums),multiply_list(filter(lambda x: x > 0, nums)),multiply_list(filter(lambda x: x < 0, nums)))

def find_min_product(nums):
    return min(multiply_list(nums),multiply_list(filter(lambda x: x > 0, nums)),multiply_list(filter(lambda x: x < 0, nums)))


def find_max_sum(nums):
    return max(sum_of_list(nums),sum_of_list(filter(lambda x: x > 0, nums)),sum_of_list(filter(lambda x: x < 0, nums)))

def find_min_sum(nums):
    return min(sum_of_list(nums),sum_of_list(filter(lambda x: x > 0, nums)),sum_of_list(filter(lambda x: x < 0, nums)))

def find_max_difference(nums):
    return max(max(nums)-min(nums),find_max_sum(nums)-find_min_sum(nums))