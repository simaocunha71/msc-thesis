"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""
class Solution:
    def __init__(self):
        self.counter = 0
        
    
    def isUnique(self, nums):
        
        if len(set(nums)) != len(nums) : #checking whether the list contains distinct values or not
            return False
            
        else:
            
            for i in range (len(nums)):
                
                self.counter += 1
                
                if nums[i] == self.counter: #if an element is repeated then count of that element will be increase, if not then it remains same
                    pass
                else :
                    
                    self.counter = 0
                    
        return True
        
print("unique_Element([1,1,1]) == ", Solution().isUnique([1,1,1]))