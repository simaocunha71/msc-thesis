```
def lps(s):
    n = len(s)
    L = [[0 for x in range(n)]for x in range(n)]
    for i in range(n):
        L[i][i] = 1
    c = 0
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                L[i][j] = 2
            elif s[i] == s[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])
    return L[0][n-1]
```    
The function lps(s) calculates the length of the longest palindromic subsequence in the given string s. It uses dynamic programming to build a 2D table L, where L[i][j] represents the length of the longest palindromic subsequence in s[i...j]. The function then returns the value at L[0][n-1], which represents the length of the longest palindromic subsequence in the entire string. The unit test assert lps("TENS FOR TENS") == 5 confirms that the function works correctly.