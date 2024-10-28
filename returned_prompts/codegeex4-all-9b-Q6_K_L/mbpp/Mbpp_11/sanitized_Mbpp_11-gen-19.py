def remove_Occ(s: str, c: str) -> str:
    if s[0] == c:
        s = s[1:]
    if s[-1] == c:
        s = s[:-1]
    return s