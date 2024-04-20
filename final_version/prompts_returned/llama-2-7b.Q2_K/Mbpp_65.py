"""
Write a function to flatten a list and sum all of its elements.
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
"""
from typing import Any, List
def recursive_list_sum(nums: List[List[Any]]) -> int:
    if type(nums) is not list : return -1
    s = 0
    for sub in nums:
        s += sum(sub)
    return s
# your code here!
# Write the Python function recursive_list_sum() that takes a list of lists and sums all the elements in those lists.
