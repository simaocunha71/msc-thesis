def remove_Occ(s, c):
    if not s or not c:
        return s
    first = s.find(c)
    last = s.rfind(c)
    if first == -1 or last == -1 or first == last:
        return s
    return s[:first] + s[first+1:last] + s[last+1:]