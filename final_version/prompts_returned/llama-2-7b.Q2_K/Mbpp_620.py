"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
class Solution:
    def largestSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        def helper(i, j):
            if i >= j:
                return 0 # i is larger than j. Return.
            
            if (nums[j] // nums[i]) > 0: # pair in list are divisble.
                return helper(i + 1, j) + 1   # continue to find largest subset from i+1 on.
            
            else: # pair is not divisible, so need to find maximum size of a subset that contains only even numbers, and then add this number back into the list.
                if helper(i - 1, j) > 0: # we can return from -1 to i without having to do anything, because the pair in question must be odd, so no change will happen here.
                    return helper(i - 1, j) + 2 # add even to the subset where ever they belong.
                else: # all previous combinations did not work out, this must be the last combination tried.
                    return helper(-1, j) + 1# add it back into the list with the remainder.
       
        def main(start_i):    
            if start_i == -1: return len(nums) # we can't go negative, so we just need to check if this is our last option.
            
            for i in range(0, len(nums), 2):    # find the largest subset that every pair (even-odd) are divisible with each other.
                helper(start_i, i + 1)  
            return len(nums)
        main(-1)
