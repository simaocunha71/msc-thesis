def remove_Occ(s, c):
    s = list(s)
    for i in range(len(s)):
        if s[i] == c:
            s[i] = ''
            break
    for i in range(len(s)-1, -1, -1):
        if s[i] == c:
            s[i] = ''
            break
    return ''.join(s)