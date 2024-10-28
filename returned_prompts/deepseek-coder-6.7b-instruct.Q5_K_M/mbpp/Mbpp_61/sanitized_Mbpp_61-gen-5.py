def count_Substrings(s):
    cnt = 0
    for length in range(1, len(s) + 1):
        for start in range(0, len(s) - length + 1):
            substr = s[start:start + length]
            if sum(int(ch) for ch in substr) == length:
                cnt += 1
    return cnt