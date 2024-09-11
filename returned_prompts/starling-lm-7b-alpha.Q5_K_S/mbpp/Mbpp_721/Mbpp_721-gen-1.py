To solve this problem, we can use dynamic programming to calculate the maximum average of paths. Here's a step-by-step explanation of how to do it:

1. Define a function `maxAverageOfPath` that takes a square matrix as input.
2. Create a 2D array `dp` of size N*N to store the maximum average of paths.
3. Initialize the first row of `dp` with the values of the first row of the matrix.
4. Initialize the first column of `dp` with the values of the first column of the matrix.
5. For each cell in the matrix starting from the second row and second column, calculate the maximum average of paths by taking the maximum of the average of the cell above and the average of the cell to the left, and add the value of the current cell. Divide the result by 2 to get the average.
6. Update the `dp` array with the calculated average.
7. Return the value at the bottom right cell of the `dp` array, which represents the maximum average of paths.

Here's the Python code for the `maxAverageOfPath` function:

```python
def maxAverageOfPath(matrix):
    N = len(matrix)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = matrix[0][0]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + matrix[i][0] / 2
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + matrix[0][j] / 2
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j] / 2
    return dp[N-1][N-1]
```

You can use this function with the example provided in the problem:

```python
print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3,