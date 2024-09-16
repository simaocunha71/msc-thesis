"""
The longest palindromic subsequence problem is a classic problem in dynamic programming. The basic idea is to create a 2D matrix to store the length of the longest palindromic subsequence in each cell of the matrix. The matrix dimensions are N x N, where N is the length of the input string.

The longest palindromic subsequence of a string of length N is the longest subsequence that is a palindrome. To find the longest palindromic subsequence, we need to consider all possible substrings of length 1 to N of the input string and find the longest one that is a palindrome.

To find the longest palindromic subsequence, we can use a dynamic programming approach. The recurrence relation for the length of the longest palindromic subsequence is as follows:

dp[i][j] = dp[i-1][j-1] + 1 if s[i] == s[j] and s[i+1...j-1] is a palindrome
dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if s[i] != s[j]
dp[i][j] = 0 if i > j

where s[i] is the i-th character of the input string.

The time complexity of this approach is O(N^2), where N is the length of the input string.
"""

def lps(s):
    N = len(s)
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1
    for i in range(N - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 2
    for j in range(2, N):
        for i in range(N - j):
            if s[i] == s[i + j]:
                dp[i][i + j] = dp[i + 1][i + j - 1] + 2
            else:
                dp[i][i + j] = max(dp[i + 1][