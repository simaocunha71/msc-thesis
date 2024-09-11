from itertools import groupby
def pack_consecutive_duplicates(L):
    return [list(it) for _, it in groupby(L)]


# Test
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
```
    
```
"""
Write a function to pack consecutive duplicates of a given list elements into sublists.
assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])==[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
"""

from itertools import groupby
def pack_consecutive_duplicates(L):
    return [list(it) for _, it in groupby(L)]
```
```

This code defines a function called `pack_consecutive_duplicates` that takes a list `L` as an argument. The function uses the `groupby` function from the `itertools` module to group consecutive duplicate elements in the list. It then converts each group into a list and returns a list of these sublists. 

The code includes a test case that checks if the function works correctly. The test case asserts that when the function is called with the list `[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]`, it should return `[[0, 0], [1], [2], [3], [4, 4