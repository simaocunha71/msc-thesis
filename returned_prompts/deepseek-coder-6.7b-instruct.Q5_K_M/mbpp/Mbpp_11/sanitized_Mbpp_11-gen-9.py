def remove_Occ(s, c):
    first = s.find(c)
    if first != -1:
        last = s.rfind(c)
        return s[:first] + s[first+1:last] + s[last+1:]
    else:
        return s