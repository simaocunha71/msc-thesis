def odd_position(lst):
    for i in range(0,len(lst),2):
        if lst[i] % 2 == 0:
            return False
    return True

odd_position([2,1,4,3,6,7,6,3])  # True






"""
Write a Python function to check if a given list of numbers contains any two numbers whose product is equal to zero.
"""
def zero_product(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            return True
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] * nums[j] == 0:
                return True
    return False

zero_product([0,2,3,0,7])  # True




"""
Given a list of strings, return a list of all the strings that contain all the characters of a target string.

For example, given the list ["hello", "world", "foobar"], and the target string "world", the function should return ["world"].
"""
def find_target(strings, target):
    result = []
    for string in strings:
        if target in string:
            result.append(string)
    return result

find_target(["hello", "world", "foobar"], "world")  # ["world"]



"""
Given a list of integers, return a new list where every integer has been multiplied by 2.
"""
def double_list(nums):
    return [num * 2 for num in nums]

double_list([1,2,3,4])  # [2,4,6,8]


"""
Given a list of integers, return a new list where all the integers are sorted in ascending order.
"""
def sort_list(nums):
    return sorted(nums)

sort_list([3,1,2])  # [1,2,3]


"""
Given a list of integers, return a