
def lps(str):
    n = len(str) 
  
    # Create a table to store results of sub-problems
    L = [[0 for x in range(n)]for y in range(n)]
  
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
  
    # Build the table using bottom-up approach.
    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (str[i] == str[j] and cl == 2):
                L[i][j] = 2
            elif (str[i] == str[j]):
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j]);
  
    return L[0][n - 1]


