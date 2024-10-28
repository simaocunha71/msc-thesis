def remove_Occ(s, char):
    return s.replace(char, '', 2) + s.replace(char, '', 1) if s else s