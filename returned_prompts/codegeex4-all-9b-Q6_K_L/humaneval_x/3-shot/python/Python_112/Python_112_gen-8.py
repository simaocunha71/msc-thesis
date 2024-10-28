    for char in c:
        s = s.replace(char, '')
    return (s, s == s[::-1])