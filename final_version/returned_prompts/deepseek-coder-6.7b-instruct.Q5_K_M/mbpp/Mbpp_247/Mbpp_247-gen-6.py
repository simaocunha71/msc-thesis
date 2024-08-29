We can solve this problem by using dynamic programming.

Here is the Python code for the problem:

```python
def lps(str):
    n = len(str)

    # Create a table to store results of subproblems
    L = [[0 for x in range(n)]for y in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    # Build the table using bottom-up approach.
    # Fill the table in a way that the length of string increases one by one
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    # L[0][n - 1] contains the length of the longest palindromic subsequence
    return L[0][n - 1]

# Test the function
print(lps("TENS FOR TENS")) # Output: 5
```

In this code, the function `lps(str)` computes the length of the longest palindromic subsequence in the given string `str`. The function uses a dynamic programming approach where it computes the length of the longest palindromic subsequence for all possible substrings of the given string. Finally, it returns the length of the longest palindromic subsequence.

For example, if the input string is "TENS FOR TENS", the function will return 5 which is the length of the longest palindromic subsequence.

Note: This code assumes that the input string is case-sensitive and spaces are considered as characters. If you want to ignore case-sensitivity, you can convert the string to either lower or upper case before calling the function. If you want to ignore spaces, you