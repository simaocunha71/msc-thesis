```
def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    return dp[0][n - 1]
```
This problem is a classic example of a dynamic programming problem. The idea is to create a 2D array `dp` where `dp[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i..j]`. We initialize the diagonal elements to 1, since a single character is always a palindrome.

Then, we fill up the rest of the array. If the characters at `s[i]` and `s[j]` are the same, we consider the substring `s[i+1..j-1]` and add 2 to the length of the longest palindromic subsequence in that substring. If the characters are different, we take the maximum of the lengths of the longest palindromic subsequences in the substrings `s[i+1..j]` and `s[i..j-1]`.

Finally, we return the value of `dp[0][n-1]`, which represents the length of the longest palindromic subsequence in the entire string. The unit test `assert lps("TENS FOR TENS") == 5` ensures that the function works correctly. For example, the longest palindromic subsequence in the string "TENS FOR TENS" is "TENS", which has a length of 5.