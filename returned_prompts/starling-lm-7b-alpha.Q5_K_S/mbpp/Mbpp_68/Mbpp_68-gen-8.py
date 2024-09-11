def is_Monotonic(nums):
    inc_flag = False
    dec_flag = False
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            inc_flag = True
        elif nums[i] > nums[i+1]:
            dec_flag = True
    if inc_flag and dec_flag:
        return False
    else:
        return True

# print(is_Monotonic([6, 5, 4, 4]))

# assert is_Monotonic([6, 5, 4, 4]) == True
# assert is_Monotonic([6, 8, 10, 15]) == True
# assert is_Monotonic([6, 8, 10, 5]) == False
# assert is_Monotonic([6, 4, 10, 15]) == True
# assert is_Monotonic([6, 4, 10, 5]) == False
# assert is_Monotonic([6, 4, 4, 10]) == True
# assert is_Monotonic([1, 1, 1, 1]) == True

"""
A monotonic array is an array that is either monotonically non-decreasing or monotonically non-increasing.

For example:

is_Monotonic([6, 5, 4, 4]) -> True
is_Monotonic([6, 8, 10, 15]) -> True
is_Monotonic([6, 8, 10, 5]) -> False
is_Monotonic([6, 4, 10, 15]) -> True
is_Monotonic([6, 4, 10, 5]) -> False
is_Monotonic([6, 4, 4, 10]) -> True
is_Monotonic([1, 1, 1, 1]) -> True
"""

"""
The is_Monotonic function takes in an array of integers, nums, and checks whether the array is monotonic or not