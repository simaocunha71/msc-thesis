"""
We will use Dynamic Programming approach to solve this problem.

First, we will create a 2D array to store the length of the longest palindromic subsequence for every possible substring of the given string.

Then, we will fill up the table in bottom-up manner.

Finally, we will return the length of the longest palindromic subsequence.

"""
def lps(str):
    n = len(str)

    # Create a table to store lengths of longest palindromic subsequences
    L = [[0 for x in range(n)]for y in range(n)]

    # Strings of length 1 are palindromes of length 1
    for i in range(n):
        L[i][i] = 1

    # Build the table in bottom up manner
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);

    return L[0][n - 1]

assert lps("TENS FOR TENS") == 5

"""
Explanation:
Longest Palindromic Subsequence is "TENET" which has length 5.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 7:
<jupyter_code>
