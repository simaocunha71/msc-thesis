"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""
from typing import List
def find_max_length(arr:List):
    max_len = 0 # 0 for the main list itself.
    temp_len = 0 # temp_len is used to track the current length of a sub-list, and then used for determining if we should use it or not.
    for i in range(0, len(arr)): # iterate over every element in the input list.
        curr_elems_len = len(arr[i]) # find out how many elements are in the current sub-list. 
        # 1. If we've already found a sub-list with more elements than the current one, then we can stop.
        if temp_len > curr_elems_len: break# 1. Else, use this new length to update our max_length variable in case we found a better one later on.
        2. If current length is shorter than last length (if there was previously no sublist to compare the current one to) then use this currents's length as "this" length and store in temp_len, else use "this" length which will be equal to the currents's length because we just used it. Then continue with i+1 which is now at (i+1).
        # 2. Else, store this current sub-list's elements into a new list called "new_sub_list". Now, update our max_length to contain "this" length and continue with the next one in range(0, len(arr)). Repeat steps 1 & 2 until we find a better one.
        # 3. else use this currents's length as "this" length and store it into temp_len before continuing to the next element (i+1) for comparison.  
    return max(arr), [arr[0]]
print("Input list:", find_max_length([[0, 3], [5, 7], [9, 11, 13]])