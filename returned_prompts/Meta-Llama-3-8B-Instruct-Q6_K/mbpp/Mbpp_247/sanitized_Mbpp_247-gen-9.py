def lps(s):
    n = len(s)
    table = [[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        table[i][i] = 1
    start = 0
    end = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            table[i][i+1] = 2
            start = i
            end = i+1
        else:
            table[i][i+1] = 0
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i+k-1
            if s[i] == s[j]:
                table[i][j] = table[i+1][j-1] + 2
                if k == 2:
                    start = i
                    end = j
                else:
                    if table[i+1][j-1] > table[start][end]:
                        start = i+1
                        end = j-1
            else:
                table[i][j] = max(table[i+1][j], table[i][j-1])
    return end-start+1