
The problem is asking to find the number of ways to arrange n elements in a sequence where each element is at most m and each element is at least twice the previous element.

Since we need to count the sequences, we can solve this problem using dynamic programming.

1. Create a 2D list dp where dp[i][j] represents the number of sequences of length i where the last element is j.

2. Fill the dp table. For each element j from 1 to m, for each length i from 2 to n, update dp[i][j] as the sum of dp[i-1][j//2] for all j//2 <= m.

3. The total number of sequences of length n is the sum of dp[n][j] for all 1 <= j <= m.

Here is the Python code for the above approach:

```python
def get_total_number_of_sequences(m, n):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(j//2, 0, -1):
                dp[i][j] += dp[i-1][k]
    return sum(dp[n])
```

In the above code, we initialize the dp table with base case where length of sequence is 1. Then, for each length from 2 to n, for each element from 1 to m, we sum up the sequences where the last element is half of the current element. Finally, we return the sum of sequences of length n.
"""

def get_total_number_of_sequences(m, n):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(j//2, 