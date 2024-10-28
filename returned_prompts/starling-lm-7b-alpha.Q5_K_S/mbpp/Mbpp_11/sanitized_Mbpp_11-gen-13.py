def remove_Occ(s: str, c: str) -> str:
    return s[s.index(c)+1:s.rindex(c)-1]