def pair_xor_Sum(nums, k):
    if not nums:
        return 0
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return k
    return pair_xor_Sum(nums[:-1], nums[-1] ^ k) + pair_xor_Sum(nums[1:], nums[0] ^ k)


def pair_xor_Sum(nums, k):
    if not nums:
        return 0
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return k
    return pair_xor_Sum(nums[:-1], nums[-1] ^ k) + pair_xor_Sum(nums[1:], nums[0] ^ k)

# print(pair_xor_Sum([5,9,7,6], 4))


# def pair_xor_Sum(nums, k):
#     if not nums:
#         return 0
#     if len(nums) == 1:
#         return 0
#     if len(nums) == 2:
#         return k
#     return pair_xor_Sum(nums[:-1], nums[-1] ^ k) + pair_xor_Sum(nums[1:], nums[0] ^ k)


"""
Write a function to calculate the sum of the XOR of all pairs of numbers in the given list.

The XOR operation is a bitwise operator that compares two bits and gives an output of 0 or 1. XOR is used to check if there are any duplicate numbers in a list.

For example, if you have a list of 10 integers, there are 45 ways to pair the numbers in the list.

The time complexity of this function is O(n^2) because for every pair, it takes O(n) time to calculate the XOR.
"""


# Here's how you can use the function:

# nums = [5,9,7,6