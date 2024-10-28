def lps(s: str) -> int:
    table = [[0 for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        table[i][i] = 1
    for cl in range(2, len(s)+1):
        for i in range(len(s)-cl+1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                table[i][j] = 2
            elif s[i] == s[j]:
                table[i][j] = table[i+1][j-1] + 2
            else:
                table[i][j] = max(table[i][j-1], table[i+1][j])
    return table[0][-1]