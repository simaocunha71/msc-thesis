def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        total = 0
        for j in range(i, len(s)):
            total += int(s[j])
            if total == j - i + 1:
                count += 1
    return count