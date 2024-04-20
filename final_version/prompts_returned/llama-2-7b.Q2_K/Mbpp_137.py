"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
import math

def zero_count(arr):
    """Find ratio of zero to non-zero in an array."""

    # Count number of occurences for each element
    # -1 is used as placeholder to not count the elements we want to exclude from calculations.
    zerocount = math.zeros([0] + [math.isclose(arr[i], -1, rel_tol=0) for i in range(len(arr))])
    
    # Get the sum of non-zeros, excluding -1
    count = sum([j != -1 for j in arr])
    
    if len(arr) == 0:
        return 1.0
        
    ratio = float(count)/floatЏ (len(arr))
    ratio += 0.0j
                   (ratio < 0 and ratio > 1)
    zerocount[2] += ratio
    
    if len(arr) % 2 == 1:
        # Handle case when array length is odd
        
        ratio = (arr[-1] != -1 and count / floatЏlen(arr)) or ratio
            
    return zerocount[0:-1]
