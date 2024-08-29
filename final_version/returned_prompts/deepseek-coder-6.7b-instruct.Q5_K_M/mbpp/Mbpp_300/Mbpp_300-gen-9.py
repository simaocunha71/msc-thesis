"""
This problem can be solved using the concept of dynamic programming.

The steps to solve this problem are:
1. Create a 2D array dp of size 2n+1 x 2n+1.
2. Initialize the first row and the first column of dp as 0.
3. For i = 1 to 2n, set dp[i][0] = 1 and dp[0][i] = 0.
4. Fill the rest of the dp array using the formula dp[i][j] = dp[i-1][j] + dp[i][j-1].
5. The count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits is dp[n][n].

Here is the Python code:
"""

def count_binary_seq(n):
    dp = [[0]*(2*n+1) for _ in range(2*n+1)]
    dp[0][0] = 1
    dp[1][0] = 1
    for i in range(2, 2*n+1):
        dp[i][0] = 0
        dp[0][i] = 0
    for i in range(1, 2*n+1):
        for j in range(1, 2*n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][n]

print(count_binary_seq(1))

"""
The time complexity of this solution is O(n^2) and the space complexity is also O(n^2).
"""
"""

