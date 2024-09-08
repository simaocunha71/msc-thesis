def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j]:
                count += 1
    return count