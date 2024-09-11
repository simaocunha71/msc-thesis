def lps(s):
    n = len(s)
    table = [[0 for x in range(n)]for x in range(n)]
    L = 0
    i = 0
    while i < n:
        if (s[i] == s[n - 1]):
            table[i][n - 1] = 2
            L += 2
            i += 1
            n -= 1
        else:
            table[i][n - 1] = 1
            i += 1
            n -= 1
    while n > 0:
        if (table[i][n - 1] == 1):
            table[i][n - 1] = 1
            i += 1
            n -= 1
        else:
            n -= 1
    return L