"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
from typing import List

def max_difference(tpl:List[int]) -> int:
    # Write your solution here.
    arr = [abs(i)-abs(j) for i, j in tpl]
    max_diff = abs(max(arr)) if len(arr) else 0
    return max_diff