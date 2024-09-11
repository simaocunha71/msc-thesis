Here is one way to do it:

```python
def lps(s):
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n):
            j = i + length - 1
            if j >= n:
                break
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
```

Here, dp[i][j] is the length of the longest palindromic subsequence in the string s[i..j]

The time complexity of this approach is O(n^2) and space complexity is also O(n^2)

To reduce the space complexity to O(n), you can use the following approach, which is based on the previous approach:

```python
def lps(s):
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [1] * n

    for length in range(2, n + 1):
        for i in range(n):
            j = i + length - 1
            if j >= n:
                break
            if s[i] == s[j]:
                dp[j] = dp[i] + 2
            else:
                dp[j] = max(dp[i + 1], dp[j])

    return dp[n - 1]
```

In this approach, we only need to keep track of the length of the longest palindromic subsequence for each position in the string, so the space