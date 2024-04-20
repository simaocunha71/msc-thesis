"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""

def pair_xor_sum(nums):
    ret = (0 if len(nums) < 2 else [])
    for idx in range(1,len(nums)):
        next_idx = (idx + 1) % len(nums)
        xor = nums[idx] ^ nums[next_idx]
        ret.append(xor)
    return sum(ret)