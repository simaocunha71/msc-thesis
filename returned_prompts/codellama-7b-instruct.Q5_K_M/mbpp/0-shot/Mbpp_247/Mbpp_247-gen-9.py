"""
def lps(s):
    # longest palindromic subsequence
    # in a string of length n
    # is a palindromic subsequence
    # of length n-1
    # in the string of length n+1
    # that is centered at index (n-1)/2
    # with the middle character removed

    # this works because we can find
    # the longest palindromic subsequence
    # of length n-1 in O(n) time
    # and then remove the middle character
    # to get the longest palindromic subsequence
    # of length n in O(n) time
    # so the total time is O(n)

    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = True

    for i in range(n):
        dp[i][i + 1] = s[i] == s[i + 1]

    for i in range(n - 1, -1, -1):
        for j in range(i + 2, n + 1):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i + 1][j] or dp[i][j - 1]

    max_len = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i][j]:
                max_len = max(max_len, j - i)

    return max_len
"""
