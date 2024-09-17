def count_Substrings(s):
    l = len(s)
    count = 0
    for i in range(l):
        for j in range(i, l):
            substring = s[i:j + 1]
            if len(substring) == sum(map(int, substring)):
                count += 1
    return count