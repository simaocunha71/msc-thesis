"""
Write a function to locate the left insertion point for a specified value in sorted order. 
assert left_insertion([1,2,4,5],6)==4
"""
class Solution:
    def leftInsert(self, nums, val):
        low=0
        for i in range(len(nums)):
            if low>=i:
                pass
            else:
                temp = nums[low]
                if val<temp:
                    return low
                elif val == temp:
                    continue
                else:
                    low+=1
        return -1