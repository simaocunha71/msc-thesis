def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if sum(int(c) for c in s[i:j+1]) == j+1:
                count += 1
    return count