"""
We can use a dynamic programming approach to solve this problem.

The function will iterate over the list of numbers and for each number, it will check all numbers before it to see if it can be divided by. If it can, it will update the maximum subset size.

Let's implement this in Python:
"""

def largest_subset(nums):
    nums.sort()
    subsets = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                subsets[i] = max(subsets[i], subsets[j] + 1)
    return max(subsets)

# Test the function
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
"""

The function works by sorting the list of numbers and initializing a list of subsets with size 1 for each number. Then it iterates over the list of numbers and for each number, it iterates over all numbers before it. If the current number can be divided by the number before it, it updates the subset size of the current number if the new size is larger. Finally, it returns the maximum subset size.
"""
"""

def largest_subset(nums):
    nums.sort()
    subsets = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                subsets[i] = max(subsets[i], subsets[j] + 1)
    return max(subsets)

# Test the function
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
