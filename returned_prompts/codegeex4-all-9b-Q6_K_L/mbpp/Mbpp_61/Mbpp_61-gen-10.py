def count_Substrings(s):
    cnt = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if sum(map(int, s[i:j])) == j - i:
                cnt += 1
    return cnt

