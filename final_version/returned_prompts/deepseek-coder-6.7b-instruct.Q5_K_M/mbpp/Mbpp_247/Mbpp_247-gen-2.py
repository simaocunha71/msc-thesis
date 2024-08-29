"""
The longest palindromic subsequence (LPS) problem is a classic computer science problem, which can be solved using dynamic programming.
The idea is to find the length of the longest palindromic subsequence in a given string.

Here is a Python solution:
"""

def lps(s):
    n = len(s)
    
    # Create a table to store the lengths of the longest palindromic subsequences.
    dp = [[0] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes of length 1.
    for i in range(n):
        dp[i][i] = 1
    
    # Check for palindromes of length 2.
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1
    
    # Check for palindromes of length 3 to n.
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1] == length-2:
                dp[i][j] = length
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]

print(lps("TENS FOR TENS")) # Output: 5
"""
In the provided string "TENS FOR TENS", the longest palindromic subsequence is "TENOT", which has a length of 5.
"""
<jupyter_output>
5
<jupyter_text>
Problem 2
<jupyter_code>
