
def lps(str):
    n = len(str)
    
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)]for y in range(n)]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
 
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process.
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

print(lps("TENS FOR TENS")) # 5


"""
Explanation:
This script calculates the length of the longest palindromic subsequence in a given string.
The dynamic programming solution iterates through the string and builds a table of the longest palindromic subsequence lengths.
The final result is the value in the top left corner of the table.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
