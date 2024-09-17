def remove_Occ(s, char):
    if char in s:
        s = s.replace(char, '', 1)
        s = s.rstrip(char)
    return s