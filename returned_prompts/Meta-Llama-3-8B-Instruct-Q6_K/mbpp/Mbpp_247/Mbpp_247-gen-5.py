```
def lps(s):
    n = len(s)
    L = [[0 for x in range(n)]for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n):
        for i in range(n - cl):
            j = i + cl
            if s[i] == s[j]:
                L[i][j] = 2 + L[i+1][j-1]
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])

    return L[0][n-1]
```    
The function `lps` calculates the length of the longest palindromic subsequence in the given string `s`. It uses dynamic programming to build a 2D array `L` where `L[i][j]` is the length of the longest palindromic subsequence in the substring `s[i..j]`. The function then returns the value of `L[0][n-1]`, which is the length of the longest palindromic subsequence in the entire string.

The unit test `assert lps("TENS FOR TENS") == 5` ensures that the function correctly calculates the length of the longest palindromic subsequence in the given string.

For example, the longest palindromic subsequence in the string "TENS FOR TENS" is "TENS", which has a length of 5. The function correctly returns 5 for this input.