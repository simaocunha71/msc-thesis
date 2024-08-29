
def count_binary_seq(n):
    # Create a table to store results of subproblems
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Initialize first row and first column of table
    for i in range(n+1):
        dp[0][i] = dp[i][0] = 1

    # Fill the table in bottom up manner
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # Return the sum of all combinations where sum of first n bits is same as sum of last n bits
    return dp[n][n] * 2

assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""

def count_binary_seq(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1

    for i in range(1, n+1):
        dp[i] = 2 * dp[i-1]

    return dp[n]

assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)

"""
