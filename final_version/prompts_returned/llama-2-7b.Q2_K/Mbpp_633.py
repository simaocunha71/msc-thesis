"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
class Solution:
    def pairWiseXOR(self, nums):
        if len(nums)<=1: return 0
        res=0
        for a in range(len(nums)): #iterate over all elements of list 'a'
            res+=int(pow(2,4-a))
        
        for b in nums[1:]: #iterate over all elements of list 'b' except for first element of list 'a'
            res+=(1^res)
            
        return res
                   
        