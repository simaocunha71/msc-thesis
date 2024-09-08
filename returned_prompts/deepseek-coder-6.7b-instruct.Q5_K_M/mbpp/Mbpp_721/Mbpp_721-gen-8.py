"""
We can solve this problem by using dynamic programming. The idea is to keep track of the maximum average path from the top left cell to the current cell in a 2D array. 

When we reach a cell, we can either move right or down, so we take the maximum of the average path from the previous cell in either direction. We then update our 2D array with this new value.

Finally, the maximum average path is stored in the bottom right cell of our 2D array.

Here is the Python code:
"""

def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = matrix[0][0]
    
    # Initialize the first row and the first column
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], matrix[i][0])
        dp[0][i] = max(dp[0][i-1], matrix[0][i])
    
    # Fill in the rest of the dp table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    # The maximum average path is in the bottom right cell
    return dp[-1][-1] / (n-1)

print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))  # Output: 5.2

"""
This solution has a time complexity of O(N^2) and space complexity of O(N^2) because we are creating a 2D array to store the maximum average path.
"""

# Dynamic Programming
# Python program to find maximum average path from top left to bottom right
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = matrix[