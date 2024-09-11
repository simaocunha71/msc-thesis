def move_zero(nums):
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1
    return nums

# Test
print(move_zero([1,0,2,0,3,4])) # [1,2,3,4,0,0]
































"""
Write a python function to move all zeroes to the end of the given list.

Explanation:
The function works by scanning the list from left to right, and when it encounters a non-zero element, it swaps that element with the element at the zero_index. Then it increments the zero_index by 1. By the end of the function, all the non-zero elements will have been moved to the left side of the list, and all the zeroes will be at the right side.
"""

"""
Assertion:
To test the function, we can use the assert statement to compare the result of the function with the expected result. In this case, we can use the assert statement to compare the result of the move_zero function with the expected result [1,2,3,4,0,0]. If the two lists are equal, the assert statement will pass and no error will be raised. Otherwise, an AssertionError will be raised, indicating that the function is incorrect.
"""

"""
Test:
To test the function, we can call the move_zero function with a sample list [1,0,2,0,3,4] and print the result. We expect the result to be [1,2,3,4,0,0], so we can compare the two lists using the == operator. If the two lists are equal, we can conclude that the function is correct.
"""

















































