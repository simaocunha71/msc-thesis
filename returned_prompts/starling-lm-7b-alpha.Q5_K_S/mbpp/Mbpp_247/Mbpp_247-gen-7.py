```
def lps(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for l in range(2, len(s)+1):
        for i in range(len(s)-l+1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][len(s)-1]
```

This function uses dynamic programming to solve the problem.
It first initializes a 2D array dp with all zeros.
Then it fills in the diagonal elements of dp with 1, since any single character in the string is a palindrome of length 1.
Next, it iterates through the lengths of substrings from 2 to the length of the string.
For each length, it iterates through all possible starting indices of substrings.
If the characters at the current indices are the same, it adds 2 to the length of the longest palindromic subsequence found so far (which is stored in dp[i+1][j-1]) and assigns the result to dp[i][j]. Otherwise, it takes the maximum length of the longest palindromic subsequence found so far (either from the right or from the left), and assigns the result to dp[i][j].
Finally, it returns the length of the longest palindromic subsequence in the original string, which is stored in dp[0][len(s)-1].

To test the function, you can use the assert statement provided in the question:
```python
assert lps("TENS FOR TENS") == 5
```
This assertion checks if the function correctly returns the length of the longest palindromic subsequence in the string "TENS FOR TENS", which is 5. If the assertion passes, it means the function is working correctly.

You can also test the function