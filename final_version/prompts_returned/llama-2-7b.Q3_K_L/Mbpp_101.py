"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
from typing import List

def kth_element(array: List[int], target: int = None) -> int:
    if not array:
        return -1
        
    # index
    idx = [0] + list(range(len(array), 0, -1))
    
    # check the target index
    if not target:
        target = min(idx)
        while target < len(array):
            if array[target] == target:
                break
            
            idx.append(target + 1)
            target += 1
        
    elif target >= len(array):
        return -1
    
    # sort the list to find the index
    list_sort = sorted(idx, reverse=True)
    if not list_sort[0] == target:
        idx.append(target + 1)
        
    return array[list_sort[-1]]
