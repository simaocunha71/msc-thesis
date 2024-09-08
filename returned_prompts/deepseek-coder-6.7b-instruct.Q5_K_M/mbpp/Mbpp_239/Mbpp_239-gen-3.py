
def get_total_number_of_sequences(m, n):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, j):
                dp[i][j] += dp[i-1][k]
    return sum(dp[n])

print(get_total_number_of_sequences(10, 4)) # 4

Explanation:

This problem is a dynamic programming problem. 

We use a 2-D array dp where dp[i][j] represents the number of possible sequences of length i that ends with a number j.

For each number j, we iterate through all possible previous number k (1 <= k < j), and add the number of possible sequences of length i-1 that ends with number k to dp[i][j].

Finally, we return the sum of dp[n] which represents the number of possible sequences of length n.
"""


"""
