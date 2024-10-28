```
def max_sum_increasing_subseq(arr, i, k, j):
    dp = [0] * len(arr)
    max_sum = 0
    for idx in range(i+1):
        dp[idx] = arr[idx]
    for idx in range(i+1, j):
        dp[idx] = max(dp[idx-1], arr[idx])
    for idx in range(j, k):
        if arr[idx] > dp[idx-1]:
            dp[idx] = arr[idx] + dp[idx-1]
        else:
            dp[idx] = dp[idx-1]
    for idx in range(k, len(arr)):
        if arr[idx] > dp[idx-1]:
            dp[idx] = arr[idx] + dp[idx-1]
        else:
            dp[idx] = dp[idx-1]
    return max(dp)
```
This function calculates the maximum sum of increasing subsequence from the prefix until ith index and also including the given kth element which is after i. It uses dynamic programming to build up the maximum sum of increasing subsequence for each index. The maximum sum is then returned. The unit test `assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11` is used to verify the correctness of the function. 














```
def max_sum_increasing_subseq(arr, i, k, j):
    dp = [0] * len(arr)
    max_sum = 0
    for idx in range(i+1):
        dp[idx] = arr[idx]
    for idx in range(i+1, j):
        dp[idx] = max(dp[idx-1], arr[idx])
    for idx in range(j, k):
        if arr[idx] > dp[idx-1]:
            dp[idx] = arr[idx] + dp[idx-1]
        else:
            dp[idx] = dp[idx-1]
    for idx in range(k, len(arr)):
        if arr[idx] > dp[idx-1]:
            dp[idx] = arr[idx] + dp[idx-1]
        else:
            dp[idx] = dp[idx-1]
    return max(dp)
```
This function calculates the maximum sum of increasing subsequence from the prefix until ith index and also including the given kth element which is after i. It uses dynamic programming to build up the maximum sum of increasing subsequence for