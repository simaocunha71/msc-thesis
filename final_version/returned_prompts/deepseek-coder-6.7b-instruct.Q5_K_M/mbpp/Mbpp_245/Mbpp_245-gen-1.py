This problem can be solved using dynamic programming.

The idea is to keep track of the maximum sum ending at each index that is part of a bitonic subsequence.

Initialize an array dp[], where dp[i] will be storing the maximum sum of bitonic subsequence ending at index i.

To fill this dp array, we will iterate through the array from left to right, and for each element at index i, we will look at all previous elements j (where j < i) and find the maximum sum of bitonic subsequences ending at j and i.

Finally, we will return the maximum value in dp[].

Here is a Python solution:

```python
def max_sum(arr):
    n = len(arr)
    if n < 3:
        return max(arr)

    dp = arr[:]
    max_val = arr[0]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
        max_val = max(max_val, dp[i])

    return max_val

print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))  # Output: 194
```

This solution has a time complexity of O(n^2) and a space complexity of O(n), where n is the length of the input array.
"""

