def remove_Occ(s, c):
    s = list(s)
    for i in range(len(s)):
        if s[i] == c:
            s[i] = ''
            break
    for i in reversed(range(len(s))):
        if s[i] == c:
            s[i] = ''
            break
    return ''.join(s)