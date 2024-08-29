def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    dp = [0]*n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i-1]*arr[i])

    return dp[-1]

print(max_product([3, 100, 4, 5, 150, 6]))  # 3000
"""
Explanation:
The subsequence with the maximum product is [100, 5, 6], the product being 100*5*6 = 3000.
"""

# Time Complexity: O(n)
# Space Complexity: O(n) for DP array, where n is the length of the input array.

# -----------------------------------------------

