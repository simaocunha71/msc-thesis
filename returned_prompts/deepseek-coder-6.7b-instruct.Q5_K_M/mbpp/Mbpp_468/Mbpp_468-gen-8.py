"""
def max_product(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] * arr[i])
    return dp[-1]

print(max_product([3, 100, 4, 5, 150, 6]))
"""

