def first_repeated_char(s):
    for i in range(len(s)):
        if s.count(s[i]) > 1 and s.index(s[i]) == i:
            return s[i]
    return None