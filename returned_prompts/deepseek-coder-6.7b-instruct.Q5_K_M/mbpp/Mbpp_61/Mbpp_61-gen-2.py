
def count_Substrings(s):
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if sum(int(ch) for ch in s[i:j+1]) == j-i+1:
                res += 1
    return res


