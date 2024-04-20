"""
Write a function to locate the left insertion point for a specified value in sorted order. 
assert left_insertion([1,2,4,5],6)==4
"""
import bisect
from typing import Optional

def left_insert(arr:Optional[List[int]], val: int):
    """Locate insertion point of a value into an array in sorted order. 
        assert left_insert([1,2,4,5],6)==4
    """ 
    if not arr:
        return None, None
    
    # bisect the list to find the location for the input val within its range
    start = bisect.bisect_left(arr,val)
    end = bisect.bisect_right(arr, val)
    
    if not arr[start] < arr[end]:
        return None, None # no such value was found in the array
    
    # locate index of the left insertion point for the input value into its specified range of sorted values
    idx = bisect.bisect_left(arr, val)
    insert_pos = (idx+1)*len(arr)+1

    return insert_pos, arr[insert_pos]