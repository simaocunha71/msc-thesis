The problem is asking for the length of the longest palindromic subsequence in a given string. A palindromic subsequence is a subsequence that reads the same backward as forward.

Here is a Python solution using dynamic programming:

```python
def lps(s):
    n = len(s)
    table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][i] = 1
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                table[i][j] = 2
            elif s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i][j - 1], table[i + 1][j])
    return table[0][n - 1]
```

This function initializes a table with zeros and then fills it up in a bottom-up manner. It checks for all possible subsequences and updates the table accordingly. Finally, it returns the value in the top-right corner of the table, which represents the length of the longest palindromic subsequence.

For example, the longest palindromic subsequence in the string "TENS FOR TENS" is "SENS", which has a length of 5. The function returns 5 for this string.