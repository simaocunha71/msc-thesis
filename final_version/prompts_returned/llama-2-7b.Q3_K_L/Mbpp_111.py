"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
from typing import List

def common_in_nested_lists(list_of_nested_list: List[List[int]]) -> List[int]:
    n = len(list_of_nested_list)
    s = set()
    if not n: return []
    
    def helper(i, j):
        if i == 0 and j == 1: return False
        
        for k in range(i-1, -1, -1):
            if k < len(list_of_nested_list[j]) - 1 and list_of_nested_list[j][k] in s:
                return True
            
            for l in range(0, k+1):
                if not helper(i-l, j-k-1) or list_of_nested_list[j][k] == list_of_nested_list[j - 1 - k]:
                    s.add(list_of_nested_list[j][k])
        return True
    
    return helper(2, n - 1)
