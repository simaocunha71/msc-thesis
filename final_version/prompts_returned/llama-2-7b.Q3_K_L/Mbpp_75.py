"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""
class Solution:
    def findDivisors(self, nums: List[int]) -> int:
        if len(nums) <= 0: return 0
        
        dict_ = {}

        for num in nums:
            if dict_.get(num):
                dict_[num] += 1
            else:
                dict_[num] = 1
            
        return sum(dict_.values())