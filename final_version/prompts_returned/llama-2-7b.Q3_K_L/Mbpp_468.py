"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
from typing import List

def max_product(arr: List[int]) -> int:
    ans = 0
    for i in range(len(arr)):
        n = arr[i]
        
        for j in range(1, i+1):
            if (n-1) * (j - 1) <= n: # (n-1), n*j < sum of all numbers from 0 to n-1 and then the first element that follows it.
                ans = max(ans, n*(n-1))
    return ans
