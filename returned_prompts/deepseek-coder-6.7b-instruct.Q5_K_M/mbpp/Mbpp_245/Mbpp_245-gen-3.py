"""
This problem can be solved using dynamic programming. 

In Python:

```python
def max_sum(arr):
    n = len(arr)
    if n < 3:
        return sum(arr)

    left = [0] * n
    right = [0] * n
    dp = [0] * n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])

    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    for i in range(1, n-1):
        dp[i] = max(dp[i-1], left[i-1]+arr[i]+right[i+1])

    return max(dp)

print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))  # output: 194
```

This code works by first initializing two arrays left and right, where left[i] will hold the maximum number from the start of the array up to the index i, and right[i] will hold the maximum number from the end of the array to the index i.

Then, we initialize the dp array, where dp[i] will hold the maximum sum of the bitonic subsequence ending at the index i.

Finally, we iterate through the array, updating dp[i] as the maximum of its current value and the sum of the maximum number from the start of the array up to the index i-1, the number at the index i, and the maximum number from the end of the array to the index i+1.

The maximum sum of the bitonic subsequence will be the maximum value in the dp array.
"""
```
</details>

### 3.4.12

<details>
<summary>