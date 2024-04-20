"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
from typing import List

def remove_consecutive(nums: List[int]):
    """
    :type nums: [int]
    :rtype: [bool]
    """
    if not nums or len(nums) == 1:
        return [True, False]
    
    def is_duplicate(index: int, num: int):
        """Is the current number a duplicate of any other numbers in the list?"""
        curr_dupe = index - 1 if index > 0 and nums[index-1] == num else False
        return curr_dupe
    
    def remove_duplicates(num: int):
        """Does the current number have any duplicates before or after it?"""
        if not is_duplicate(index, num) or index > 0 and nums[index-1] == num:
            return True
            
        return False
    
    def remove_duplicates_recursive(nums):
        """Helper function for recursion."""
        count = len(nums) - 2 if not is_duplicate(0, nums[0]) else None
        
        dups = set()
        curr_dupe = []
        
        for i in range(len(nums)):
            if remove_duplicates(int(nums[i])):
                dups.add(int(nums[i]))
            
            elif nums[i] == 0 and count is None: # No duplicate for 0, so return empty list
                return []
                    
        if len(dups) > 1:
            dupe_index = [i for i in range(len(nums)) if int(nums[i]) in dups][-1]
            
            nums.append(0) # Add a dummy to the beginning of list
            curr_dupe = [] # Remove the current duplicate
            
            while len(curr_dupe) == 0:
                i += 1
                
                if dups[int(nums[i])] or int(nums[i-1]) in dups and is_duplicate(dupe_index, nums[dupe_index + 1]