def remove_Occ(s, ch):
    # remove first occurrence
    s = s.lstrip(ch)
    # remove last occurrence
    s = s.rstrip(ch)
    return s