def remove_Occ(s, char):
    if char not in s:
        return s
    s = s.replace(char, '', 2)
    return s