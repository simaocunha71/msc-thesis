def rotate_right(nums, k):
    def rotate(nums, k):
        nums.insert(0, nums.pop(len(nums)-k))
    for _ in range(k):
        rotate(nums, 1)
    return nums

# def rotate_right(nums, k):
#     def rotate(nums, k):
#         tmp = nums.pop()
#         nums.insert(0, tmp)
#         for i in range(len(nums)):
#             if nums[i] == tmp:
#                 nums.pop(i)
#                 break
#     for _ in range(k):
#         rotate(nums, 1)
#     return nums

# def rotate_right(nums, k):
#     for _ in range(k):
#         tmp = nums.pop()
#         nums.insert(0, tmp)
#     return nums

# print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

# print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

# print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))


"""
Write a function to determine if a given number is strong or not. A number is strong if it has factorial digits. 

For example: 

14 is strong because 1! + 4! = 1 + 24 = 25
132 is strong because 1! + 3! + 2! = 1 + 6 + 2 = 9

But 

123 is not strong


Hint: 

You can use Python's factorial function.
You can use Python's sum function.


Test cases:

assert is_strong(14) == True
assert is