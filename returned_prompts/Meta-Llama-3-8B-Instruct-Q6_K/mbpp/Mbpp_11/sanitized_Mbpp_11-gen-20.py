def remove_Occ(s, char):
    if char not in s:
        return s
    s = list(s)
    if s[0] == char:
        s.pop(0)
    if s[-1] == char:
        s.pop()
    return "".join(s)