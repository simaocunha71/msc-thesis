def replace_char(s, c1, c2):
    for i in range(len(s)):
        if s[i] == c1:
            s = s[:i] + c2 + s[i+1:]
    return s