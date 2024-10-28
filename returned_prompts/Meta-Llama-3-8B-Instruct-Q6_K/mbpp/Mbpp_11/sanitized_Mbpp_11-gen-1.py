def remove_Occ(s, char):
    return s.replace(char, '', 2) if s.count(char) >= 2 else s