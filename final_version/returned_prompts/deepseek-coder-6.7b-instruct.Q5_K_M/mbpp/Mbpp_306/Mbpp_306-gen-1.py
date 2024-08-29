This problem can be solved by using dynamic programming.

First, initialize two lists (dp and index) with the same length of input array. dp stores the maximum sum of increasing subsequence, and index stores the index of the previous number in the increasing subsequence.

Then, for each number in the array, find the maximum sum of increasing subsequence ending with this number by comparing the sum of its increasing subsequences ending with all previous numbers. If the sum is greater, update dp and index.

Finally, to find the maximum sum of increasing subsequence from prefix until ith index and including the kth element, we need to find the maximum sum of increasing subsequence ending with the kth element and the maximum sum of increasing subsequence ending with the ith element.

Here is the python code for this problem:

```python
def max_sum_increasing_subseq(arr, n, i, k):
    dp = [0]*n
    index = [-1]*n
    max_sum = 0
    max_index = -1

    for j in range(n):
        for l in range(j):
            if arr[l] < arr[j] and dp[l] > dp[j]:
                dp[j] = dp[l]
                index[j] = l
        dp[j] += arr[j]
        if dp[j] > max_sum:
            max_sum = dp[j]
            max_index = j

    if k >= i:
        return max_sum

    prefix_sum = [0]
    for p in range(i):
        prefix_sum.append(prefix_sum[-1] + arr[p])

    max_sum_prefix_k = prefix_sum[k]
    while max_index >= 0:
        if index[max_index] >= i:
            max_sum_prefix_k = max(max_sum_prefix_k, prefix_sum[index[max_index]+1] + arr[max_index])
        max_index = index[max_index]

    return max_sum_prefix_k
```

This function returns the maximum sum of increasing subsequence from prefix until ith