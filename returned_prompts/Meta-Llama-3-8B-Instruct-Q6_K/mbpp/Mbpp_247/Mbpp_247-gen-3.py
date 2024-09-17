```
def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
```


This function uses dynamic programming to find the length of the longest palindromic subsequence in the given string. It first initializes a 2D array dp where dp[i][j] represents the length of the longest palindromic subsequence in the substring s[i..j]. Then it fills up the dp array in a bottom-up manner. The function returns the value of dp[0][n-1] which is the length of the longest palindromic subsequence in the given string.

The unit test `assert lps("TENS FOR TENS") == 5` ensures that the function returns the correct length of the longest palindromic subsequence. In this case, the longest palindromic subsequence is "TENS" which has a length of 5.