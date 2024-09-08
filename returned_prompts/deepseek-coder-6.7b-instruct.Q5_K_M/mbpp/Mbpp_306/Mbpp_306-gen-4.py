"""
def max_sum_increasing_subseq(arr: List[int], n: int, k: int, i: int) -> int:
    dp = [0] * n
    dp[i] = arr[i]
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + arr[j])
            i = j
    dp[k] = max(dp[k], dp[i] + arr[k])
    return max(dp)

assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
"""

