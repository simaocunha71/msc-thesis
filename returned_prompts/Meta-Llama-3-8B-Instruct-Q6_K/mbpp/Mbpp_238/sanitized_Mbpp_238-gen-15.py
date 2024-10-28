def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1].strip():
                count += 1
    return count