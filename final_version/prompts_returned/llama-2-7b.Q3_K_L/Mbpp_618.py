"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
class Solution:
    def __init__(self):
        self.dict = {}
    
    def elementWiseDivision(self, nums1: List[int], nums2:List[int]) -> List[float]:
        new_nums = [] 
        for i in range(len(nums1)):
            if i in self.dict:
                self.dict[i] += 1 
            else: 
                self.dict[i] = 0  
            
            nums2_index = self.dict.get(nums2[-1], 0)
            new_nums.append((int)(float(nums1[i])/nums2_index))
    
        return new_nums
        