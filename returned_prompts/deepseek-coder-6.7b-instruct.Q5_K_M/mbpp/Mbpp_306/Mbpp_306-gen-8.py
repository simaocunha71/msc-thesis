
The problem can be solved by using dynamic programming. We start by initializing an array dp of size n+1 with all elements as 0 (where n is the length of the input array). For each index i in the input array from 0 to n-1, we check each index j in the input array from i+1 to n. If arr[j] > arr[i] and j>i+k, we update dp[j] as max(dp[j], dp[i]+arr[j]). After checking all the possible pairs, the maximum sum of increasing subsequence is the maximum value in the dp array.

Here is the Python code for the problem:

```python
def max_sum_increasing_subseq(arr, n, k, i):
    dp = [0] * (n+1)
    for j in range(i+1, n):
        for l in range(i, j):
            if arr[j] > arr[l] and l>i+k:
                dp[j] = max(dp[j], dp[l]+arr[j])
    return max(dp)

print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6))  # 11
```

In this code, we first initialize the dp array with all elements as 0. Then we start from the (i+1)th index of the array and for each index j, we check all the previous indexes l. If arr[j] > arr[l] and l is greater than i+k, we update the dp[j] with the maximum of dp[j] and dp[l]+arr[j]. Finally, we return the maximum value in the dp array.

Please note that the time complexity of this code is O(n^2) and the space complexity is O(n). So, it may not be efficient for large inputs.
"""

"""
