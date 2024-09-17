```
def max_sum_increasing_subseq(arr, i, k, j):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for idx in range(n + 1):
        dp[idx][0] = 0
    for idx in range(1, n + 1):
        for jdx in range(1, min(idx + 1, k + 1)):
            if jdx == 1:
                dp[idx][jdx] = dp[idx - 1][jdx]
            else:
                dp[idx][jdx] = max(dp[idx - 1][jdx], dp[idx - 1][jdx - 1] + arr[idx - 1])
    return dp[n][k]
```

Explanation:
The function `max_sum_increasing_subseq` takes four parameters: `arr` (the array), `i` (the current index), `k` (the kth element), and `j` (the current sum). It returns the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i.

The function initializes a 2D array `dp` with size `(n + 1) x (k + 1)`, where `n` is the length of the array. The base case is that the maximum sum is 0 when `idx` is 0 or `jdx` is 0.

Then, for each `idx` from 1 to `n`, and for each `jdx` from 1 to `k`, the function calculates the maximum sum by considering two options: either include the current element in the increasing subsequence or not. If `jdx` is 1, it means we are considering the first element in the increasing subsequence, so the maximum sum is the same as the previous maximum sum. If `jdx` is greater than 1, it means we are considering an element that is greater than the previous element in the increasing subsequence, so the maximum sum is the maximum of the previous maximum sum and the sum of the previous maximum sum and the current element.

Finally, the function returns the maximum sum at the last row and column of the `dp` array, which represents the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i. The unit test `assert max_sum