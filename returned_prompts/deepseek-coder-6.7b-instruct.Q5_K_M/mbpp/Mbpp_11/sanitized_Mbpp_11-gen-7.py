def remove_Occ(s, ch):
    return s[:s.find(ch)] + s[s.rfind(ch) + 1:]