
def count_Substrings(s):
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if sum(map(int, s[i:j + 1])) == j - i + 1:
                ans += 1
    return ans


