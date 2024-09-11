```
def lps(s):
    n = len(s)
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i + 1][j], table[i][j - 1])
    return table[0][n - 1]
```

Here's the step-by-step logic behind this solution:

1. The algorithm is based on the concept of constructing the longest palindromic subsequence.

2. It starts by initializing a 2D table of size `n` by `n`, where `n` is the length of the given string `s`. Each element in the table represents the length of the longest palindromic subsequence for a substring of `s`.

3. The algorithm then fills in the table by iterating over all possible substrings of `s`. For each substring, it checks if the first and last characters are the same. If they are, it adds 2 to the length of the longest palindromic subsequence of the substring obtained by removing the first and last characters. If they are not the same, it takes the maximum length from the substring obtained by removing the first character or the substring obtained by removing the last character.

4. Finally, the algorithm returns the length of the longest palindromic subsequence, which is stored in the top-right element of the table.

5. The provided assertion `lps("TENS FOR TENS") == 5` verifies that the function correctly computes the length of the longest palindromic subsequence for the given string.

Here's an example usage of the `lps` function:
```python
s = "TENS FOR TENS"
print(lps(s))  # Output: 5
```