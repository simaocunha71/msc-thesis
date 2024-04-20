"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""
# Solution
def count_pairs(nums):
    for i in nums:
        if i > 0:
            return (i*(len(nums)-1))-(i-1)*(len(nums)-1)
