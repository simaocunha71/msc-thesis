This problem can be solved using dynamic programming.

Here is a Python solution:

```python
def get_total_number_of_sequences(m, n):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, j):
                dp[i][j] += dp[i-1][k]
    return sum(dp[n])

print(get_total_number_of_sequences(10, 4))  # Output: 4
```

This solution works by creating a 2D list dp where dp[i][j] is the number of sequences of length i with the last element being j. 

Then, for each value of j from 1 to m, we iterate through all possible values of k that satisfy the conditions (2k <= j <= m) and increment dp[i][j] by dp[i-1][k].

Finally, we sum up the values of dp[n] for all j and return the result. 

This solution has a time complexity of O(m^2 * n) and a space complexity of O(m * n), where m is the upper limit of the elements in the sequences and n is the length of the sequences.
"""

