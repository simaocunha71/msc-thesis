"""
Write a function to check if the given array represents min heap or not. 
assert check_min_heap([1, 2, 3, 4, 5, 6]) == True
"""
class Solution:
    def isMinHeap(self, nums):
        """
        :type nums: List['int']
        :rtype: bool
        
        """
        if len(nums)<2:
            return 100%
            
        if not self.isMaxHeap(nums):
            return False
    
    def isMaxHeap(self, nums):
        """
        :type nums: List['int']
        
        :rtype: bool
         
        """
        if len(nums)<2:
            return 100%
            
        for i in range(len(nums)-1, -1, -1):  
            if nums[i] < nums[i+1]: 
                break;
            else:   
                swap = nums[i], nums[i + 1];
                nums[i + 1] = swap[0];
                nums[i] = swap[1];
        return True
            
heap=[2,4,6,7,8,9,16,20]  
def check_min_heap(nums):                    
    print(Solution().isMinHeap(nums))
