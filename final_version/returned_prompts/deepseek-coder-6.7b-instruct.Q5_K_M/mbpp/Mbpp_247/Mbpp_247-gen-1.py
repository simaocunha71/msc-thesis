Here is a Python solution using dynamic programming:

```python
def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]

print(lps("TENS FOR TENS"))
```

This solution works by building up a table of longest palindromic subsequence lengths, dp[i][j], for all substrings of s. For each substring, it checks if the first and last characters are the same. If they are, it adds 2 to the length of the longest palindromic subsequence of the substring without the first and last characters. If they are not the same, it takes the maximum of the longest palindromic subsequence of the substring without the first character and the longest palindromic subsequence of the substring without the last character. The final result is in dp[0][n-1], which is the length of the longest palindromic subsequence of the entire string.
"""


# 