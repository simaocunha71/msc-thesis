def remove_Occ(s, ch):
    idx = s.find(ch)
    idx1 = s.rfind(ch)
    if idx == -1 or idx1 == -1:
        return s
    return s[:idx] + s[idx + 1:idx1] + s[idx1 + 1:]