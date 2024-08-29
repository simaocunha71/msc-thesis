def remove_Occ(s, ch):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ch:
            s[i] = ''
            break
    for i in range(len(s)-1, -1, -1):
        if s[i] == ch:
            s[i] = ''
            break
    return ''.join(s)