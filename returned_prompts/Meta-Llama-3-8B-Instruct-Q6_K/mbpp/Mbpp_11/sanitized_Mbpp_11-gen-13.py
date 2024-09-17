def remove_Occ(s, char):
    s = list(s)
    if s[0] == char:
        s.pop(0)
    if s and s[-1] == char:
        s.pop()
    return ''.join(s)