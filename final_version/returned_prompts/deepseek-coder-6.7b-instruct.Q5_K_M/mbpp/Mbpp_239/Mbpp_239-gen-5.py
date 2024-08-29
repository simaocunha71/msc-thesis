
"""
Explanation: 

The sequences are:
(2, 4, 8, 16),
(2, 4, 8, 10),
(2, 4, 12, 16),
(2, 6, 8, 16),
(2, 6, 8, 10),
(2, 6, 12, 16),
(2, 8, 12, 16),
(4, 8, 12, 16)

So, the function should return 8.
"""

def get_total_number_of_sequences(m, n):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, j//2+1):
                dp[i][j] += dp[i-1][k]
    return sum(dp[n])

print(get_total_number_of_sequences(10, 4))  # 8

# Time complexity: O(n*m^2)
# Space complexity: O(n*m)
<jupyter_output>
8
<jupyter_text>
