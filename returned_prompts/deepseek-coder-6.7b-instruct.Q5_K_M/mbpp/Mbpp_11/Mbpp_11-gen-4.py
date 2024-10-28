
def remove_Occ(s, ch):
    f = s.find(ch)
    if f != -1:
        s = s[:f] + s[f+1:]
        s = s.rstrip(ch)
    return s


