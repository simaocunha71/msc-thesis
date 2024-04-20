"""
Write a python function to check whether every odd index contains odd numbers of a given list.
assert odd_position([2,1,4,3,6,7,6,3]) == True
"""
class Solution:
    def oddPosition(self, nums):
        if not isinstance(nums, (list, tuple)):
            return False
        
        # We use a map to ensure that there is no duplicate for the same index.
        pos_dict = {}
        count = 0
        res = True
        
        for i in range(1, len(nums)):
            
            if nums[i] % 2 == 1:
                # If current odd is different from prev even, then it is the right position.
                pos_dict[i] = count
                
                # Check whether the odd number that we want is already in the list.
                for j in range(len(nums)):
                    if nums[j] == i and (pos_dict[j] or not j % 2):
                        return False   # Error!
            
            count += 1
        
        # Check whether the current odd element is not found in the list.
        for k, v in pos_dict.items():
            if nums[k] != i and (pos_dict[k + 1] or True) and nums[k+1] % 2 == 1:
                return False   # Error!
                
        return res   # All is well!
```