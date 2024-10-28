def remove_Occ(s, char):
    if char not in s:
        return s
    else:
        return s.replace(char, '', 2)