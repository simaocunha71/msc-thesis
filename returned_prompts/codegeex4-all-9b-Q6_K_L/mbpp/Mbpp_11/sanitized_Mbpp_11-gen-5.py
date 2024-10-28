def remove_Occ(s, ch):
    if len(s) < 2:
        return s
    if s[0] == ch:
        s = s[1:]
    if s[-1] == ch:
        s = s[:-1]
    return s