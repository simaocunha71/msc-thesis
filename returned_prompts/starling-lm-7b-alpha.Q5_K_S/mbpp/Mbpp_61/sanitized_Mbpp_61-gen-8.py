def count_Substrings(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if sum(map(int, s[i:j + 1])) == j - i + 1:
                res += 1
    return res