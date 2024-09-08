def lps(s):
    n = len(s)

    # Create a table to store lengths of longest palindromic subsequence
    dp = [[0 for x in range(n)] for x in range(n)]

    # Strings of length 1 are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Check for substring of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    # Check for substrings of length 3 to n
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and length == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    return dp[0][n-1]