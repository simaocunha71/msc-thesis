"""
We can solve this problem by using dynamic programming.
First, let's understand the problem. We need to find binary sequences of length 2n such that the sum of the first n bits equals the sum of the last n bits.

To solve this problem, we can start by defining a 2D array dp[n+1][2*n+1] where dp[i][j] will be storing the count of binary sequences of length 2i such that the sum of the first i bits equals the sum of the last i bits.

Then, we will initialize dp[0][0] to 1 because there is only one binary sequence of length 0 such that the sum of the first 0 bits equals the sum of the last 0 bits.

Then, we will fill up the dp table in a bottom-up manner. For each i from 1 to n, and for each j from 0 to 2*n, we will calculate dp[i][j] as the sum of dp[i-1][j-1] and dp[i-1][j+1].

Finally, the answer will be the sum of dp[n][j] for all j from n to 2n.

This solution has a time complexity of O(n^2) and a space complexity of O(n^2).
"""

def count_binary_seq(n):
    dp = [[0]*(2*n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(2*n+1):
            dp[i][j] = dp[i-1][j-1] if j-1 >= 0 else 0
            dp[i][j] += dp[i-1][j+1] if j+1 <= 2*n else 0
    return sum(dp[n][n:2*n+1])

# Test the function
print(math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001))
"""

The function should return True for the test case.
"""
<jupy