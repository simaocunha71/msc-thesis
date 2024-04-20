"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
import math

def max_product(arr):
    n = len(arr) # length
    prod = 1
    cur_max = arr[n-2]
    for i in range(n-2, -1, -1):
        prod *= arr[i] if arr[i] > cur_max else (prod//=cur_max)
    
    return max(map(math.fabs, map(lambda x: math.fabs(x), list(range(-1,-n+2))))) * prod