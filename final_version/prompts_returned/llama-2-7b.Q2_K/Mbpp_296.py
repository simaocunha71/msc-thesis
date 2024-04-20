"""
Write a python function to count inversions in an array.
assert get_Inv_Count([1,20,6,4,5]) == 5
"""
from typing import Optional
def get_Inv_Count(arr: list[Optional[int]]):
    inv_count = [0] * len(arr)  # set default to zero on all indices
    for i in range(len(arr)):
        if arr[i] > i:   # if number at index is greater than its index, count one inversion
            inv_count[i] += 1
    return inv_count
    
print('-'*60)
# call function to get output in place of input
print(get_Inv_Count([1,2,3]))
