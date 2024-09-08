
def move_zero(lst):
    non_zero = [num for num in lst if num != 0]
    count = len(lst) - len(non_zero)
    return non_zero + [0]*count

print(move_zero([1,0,2,0,3,4]))

"""
This function works by creating a new list with only the non-zero numbers from the original list. It then counts how many zeroes were in the original list (by subtracting the length of the new list from the original's length). Finally, it appends this number of zeroes to the end of the new list.
"""

"""
Others can also do it using a two-pointer approach, where one pointer iterates the list and the other one points to the last non-zero element seen in the list.
"""

def move_zeroes(nums):
    last_non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_index] = nums[i]
            last_non_zero_index += 1

    for i in range(last_non_zero_index, len(nums)):
        nums[i] = 0

    return nums

print(move_zeroes([1,0,2,0,3,4]))

"""
This function works by first identifying all non-zero numbers and placing them at the front of the list, then it fills the rest of the list with zeros.
"""
<jupyter_output>
[1, 2, 3, 4, 0, 0]
[1, 2, 3, 4, 0, 0]
<jupyter_text>
Question 2
<jupyter_code>
