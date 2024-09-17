def remove_Occ(s, c):
    return s[s.index(c)+1:len(s)-s[::-1].index(c)]