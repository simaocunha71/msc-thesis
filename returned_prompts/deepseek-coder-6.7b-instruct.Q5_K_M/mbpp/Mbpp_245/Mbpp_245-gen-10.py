"""
The task can be divided into two parts:
1. Find the increasing subsequence.
2. Find the decreasing subsequence.

Then, we can find the maximum sum of bitonic subsequence by adding the maximum sum of the increasing and decreasing subsequence.
"""

Python Code:

```python
def max_sum(arr):
    n = len(arr)
    
    # Find the increasing subsequence.
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j]+1:
                lis[i] = lis[j]+1
    
    # Find the decreasing subsequence.
    lds = [1]*n
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and lds[i] < lds[j]+1:
                lds[i] = lds[j]+1
    
    # Find the maximum sum of bitonic subsequence.
    max_sum = max(lis[i] + lds[i] - 1 for i in range(n))
    return max_sum

print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))  # Output: 194
```

In this code, we first create two lists `lis` and `lds` to store the longest increasing subsequence and the longest decreasing subsequence. Then, we compute the maximum sum of bitonic subsequence by adding the maximum sum of the increasing and decreasing subsequence. The maximum sum is the maximum value in the list of the sum of `lis[i]` and `lds[i]`, where `i` is the index of the array.
"""

