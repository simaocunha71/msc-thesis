"""
def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                if s[i] == s[j]: dp[i][j] = 2
                else: dp[i][j] = 0
            else:
                if s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1] + 2
                else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]
"""

def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n): dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                if s[i] == s[j]: dp[i][j] = 2
                else: dp[i][j] = 0
            else:
                if s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1] + 2
                else: dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


def test():
    assert lps("TENS FOR TENS") == 5
    assert lps("") == 0
    assert lps("ABCD") == 2
    assert lps("ABBA") == 3
    assert lps("BABAC") == 5
    assert l