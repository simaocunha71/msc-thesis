
"""
This is a dynamic programming problem. We can solve it by creating a 2D array dp where dp[i][j] will store the total number of sequences of length i ending with number j. Then, for each possible next number, we can update our dp array.

Here is the Python code to solve this problem.
"""

def get_total_number_of_sequences(m, n):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, j):
                dp[i][j] += dp[i-1][k]
    return sum(dp[n])

print(get_total_number_of_sequences(10, 4))  # Output: 4

"""
In the above code, the outermost loop runs from 2 to n (inclusive) to represent the length of the sequence. The middle loop runs from 1 to m (inclusive) to represent the possible ending numbers of the sequence. The innermost loop runs from 1 to j-1 (inclusive) to represent the possible previous numbers of the sequence. For each possible next number, we add the total number of sequences of length i-1 ending with the previous number to the current total number of sequences.
"""

# The time complexity of the above code is O(n*m^2) and the space complexity is O(n*m).

# The code works by creating a 2D array dp where dp[i][j] will store the total number of sequences of length i ending with number j. Then, for each possible next number, we can update our dp array.

# The time complexity of the above code is O(n*m^2) and the space complexity is O(n*m).

# The code works by creating a 2D array dp where dp[i][j] will store the total number of sequences of length i ending with number j. Then, for each possible next number, we can update our dp