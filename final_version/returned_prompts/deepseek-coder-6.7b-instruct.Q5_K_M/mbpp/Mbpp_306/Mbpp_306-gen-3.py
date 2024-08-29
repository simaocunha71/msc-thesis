
def max_sum_increasing_subseq(arr, n, i, k):
    dp = [0]*n
    dp[i] = arr[i]
    max_sum = dp[i]

    for j in range(i+1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + arr[j])
            max_sum = max(max_sum, dp[j])

    dp[k] = max(dp[k], arr[k])
    for j in range(k+1, n):
        if arr[j] > arr[k]:
            dp[j] = max(dp[j], dp[k] + arr[j])
            max_sum = max(max_sum, dp[j])

    return max_sum

print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6))  # 11

Explanation: The maximum sum of increasing subsequence is 11 ([1, 2, 3, 4, 5] or [1, 2, 3, 6] or [1, 2, 100, 101] or [1, 4, 100, 101] or [1, 5, 100, 101] or [1, 101]).
"""

def max_sum_increasing_subseq(arr, n, i, k):
    dp = [0]*n
    dp[i] = arr[i]
    max_sum = dp[i]

    for j in range(i+1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + arr[j])
            max_sum = max(max_sum, dp[j])

    dp[k] = max(dp[k], arr[k])