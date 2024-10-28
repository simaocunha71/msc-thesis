def remove_Occ(s, c):
    if c not in s:
        return s
    return s.replace(c, '', 2) + c