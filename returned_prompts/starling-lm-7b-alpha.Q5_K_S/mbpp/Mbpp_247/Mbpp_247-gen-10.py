def lps(s):
    dp = [[0 for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s)-1, 0, -1):
        for j in range(i, len(s)):
            if s[i-1] == s[j]:
                dp[i-1][j] = dp[i][j] + 1
            else:
                dp[i-1][j] = max(dp[i][j], dp[i-1][j-1])
    return dp[0][-1]

lps("TENS FOR TENS")  # 5
# This problem can be solved by using DP,
# the key point is to find the longest palindromic sequence in the string,
# and then we can use the DP method to find the length of the longest palindromic subsequence.
"""
The idea of DP is to use the previous results to compute the current results,
and we use a DP table to store the results of all subproblems,
and we use the current result to update the previous result.
"""

# Finally, we can return the result of the last subproblem.
# We can see that this is a typical DP problem, which can be solved using DP.

"""
The problem can be solved by using dynamic programming.
The key is to find the longest palindromic subsequence in the string.
We can use the dynamic programming method to find the length of the longest palindromic subsequence.

The idea of dynamic programming is to use the previous results to compute the current results,
and we use a DP table to store the results of all subproblems,
and we use the current result to update the previous result.

Finally, we can return the result of the last subproblem.

This is a typical dynamic programming problem, which can be solved using dynamic programming.
"""

"""
In this problem, we need to find the longest palindromic subsequence in a given string.

The key idea is to find the longest palindromic subsequence