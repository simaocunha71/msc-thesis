"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""

def second_smallest(nums):
    n = len(nums)

    def helper(i, j):
        if i == j and nums[i] > 0: return True
        elif i >= j or not helper(j+1, i-1): return False
        else: return True
        
    for i in xrange(n-2,-1,-1):
        if helper(i, i): return nums[i]
    
second_smallest([1, 2]) #2
