
def find_even_pair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] ^ nums[j] % 2 == 0:
                count += 1
    return count
"""
The inner loop starts from i+1 because we cannot pair a number with itself.
XOR operation on two numbers returns an even number if and only if both numbers are even or both numbers are odd.
"""

