"""
This problem can be solved using dynamic programming. We will create a table dp[j][i] which stores the length of the longest palindromic subsequence in string[i..j].
We will fill this table in a bottom-up manner, i.e., filling the table from smaller substrings to larger ones.
We will fill the table in following manner:
- If string[i] == string[j], then dp[j][i] = dp[j-1][i+1] + 2
- If string[i] != string[j], then dp[j][i] = max(dp[j-1][i], dp[j][i+1])
Finally, we will return dp[n-1][0] where n is the length of the string.
"""

def lps(string):
    n = len(string)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Strings of length 1 are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Check for length 2 palindromes
    for i in range(n-1):
        if string[i] == string[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    # Check for lengths greater than 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

print(lps("TENS FOR TENS"))  # Output: 5
"""

