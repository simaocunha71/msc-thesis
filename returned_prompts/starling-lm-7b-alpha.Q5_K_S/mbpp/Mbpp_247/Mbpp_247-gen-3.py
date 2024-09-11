```
def lps(s):
    n = len(s)
    table = [[0]*n for _ in range(n)]
    for i in range(n):
        table[i][i] = 1
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                table[i][j] = table[i+1][j-1] + 2
            else:
                table[i][j] = max(table[i+1][j], table[i][j-1])
    return table[0][n-1]
```

Here's a function that computes the length of the longest palindromic subsequence in a given string.
The function `lps` takes a string `s` as input and returns the length of the longest palindromic subsequence in `s`.
The algorithm used in the function is dynamic programming, specifically the longest common subsequence (LCS) algorithm.
The algorithm creates a table of size `n` by `n`, where `n` is the length of the string.
The table is initialized with zeros, and the diagonal of the table is set to 1, as each character in a string is a palindrome of length 1.
Then, the algorithm iterates over the table in reverse order, starting from the second-to-last character and moving towards the first character.
For each pair of characters `(i, j)` in the string, if the characters are the same, the length of the palindromic subsequence is incremented by 2, as the current characters can be part of a longer palindrome.
If the characters are not the same, the length of the palindromic subsequence is determined by taking the maximum of the length of the subsequence obtained by excluding the current character (`table[i+1][j]`) and the length of the subsequence obtained by excluding the current character (`table[i][j-1]`).
Finally, the function returns the length of the longest palindromic subsequence, which is stored in the top-left cell of the table (`table[0][n-1]`).
