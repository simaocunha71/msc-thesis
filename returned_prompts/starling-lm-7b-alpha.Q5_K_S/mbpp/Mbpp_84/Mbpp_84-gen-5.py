from itertools import combinations
import math

def sequence(n):
    if n < 1:
        return "Input must be a positive integer"
    else:
        n = int(n)
        if n == 1:
            return 1
        else:
            nums = [1, 1]
            for i in range(2, n):
                nums = list(map(sum, combinations(nums, 2)))
                nums = sorted(nums)
                if nums[-1] == 1:
                    nums = nums[:-1]
            return nums[-1]

# def sequence(n):
#     if n < 1:
#         return "Input must be a positive integer"
#     else:
#         n = int(n)
#         if n == 1:
#             return 1
#         else:
#             nums = [1, 1]
#             for _ in range(n - 2):
#                 nums = list(map(sum, combinations(nums, 2)))
#                 nums = sorted(nums)
#                 if nums[-1] == 1:
#                     nums = nums[:-1]
#             return nums[-1]

# def sequence(n):
#     if n < 1:
#         return "Input must be a positive integer"
#     else:
#         n = int(n)
#         if n == 1:
#             return 1
#         else:
#             nums = [1, 1]
#             for _ in range(n - 2):
#                 nums = [num + num2 for num in nums for num2 in nums]
#                 nums = sorted(nums)
#                 while nums[-1] == 1:
#                     nums = nums[:-1]
#             return nums[-1]

# def sequence(n):
#     if n < 1:
#         return "Input must be a positive integer"
#     else:
#         n = int(n)
#         if n == 1: