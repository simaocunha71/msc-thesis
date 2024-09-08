def lps(string):
    n = len(string)

    # Create a table to store results of sub-problems
    L = [[0 for x in range(n)]for y in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The process is filled
    # in a manner such that L[i][j] contains length of the longest
    # palindromic subsequence.
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if string[i] == string[j] and cl == 2:
                L[i][j] = 2
            elif string[i] == string[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);

    return L[0][n - 1]