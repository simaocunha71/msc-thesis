"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""
from typing import List

def pack_consecutive_duplicates(lst:List[int]) -> List[List]:
    length = len(lst)
    result = []

    for i in range(0, length//2-1):
        if lst[i] == lst[i+1]:
            result.append([lst[i], lst[i+1]])
            
            #print('',end='')
    
    return result