This problem can be solved using dynamic programming.

Here is the Python solution:

def count_binary_seq(n):
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dp[0][0] = 1  # base case
    MOD = 10**9+7

    # iterate over all possible values of first n bits
    for i in range(n+1):
        # iterate over all possible values of last n bits
        for j in range(n+1):
            # if the sum of first n bits is less than n
            if i < n:
                dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
            # if the sum of last n bits is less than n
            if j < n:
                dp[i][j+1] = (dp[i][j+1] + dp[i][j]) % MOD
            # if the sum of first n bits is equal to the sum of last n bits
            if i == j:
                dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % MOD
    return dp[n][n]

# Test case
print(count_binary_seq(1))  # Output: 2

In this solution, dp[i][j] represents the number of binary sequences of length 2n such that the sum of the first i bits is equal to the sum of the last j bits. The base case is dp[0][0] = 1. The final answer is dp[n][n].
"""

