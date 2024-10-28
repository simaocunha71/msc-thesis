def remove_Occ(s, c):
    first = s.find(c)
    last = s.rfind(c)
    if first == last:
        return s[:first] + s[first+1:]
    else:
        return s[:first] + s[first+1:last] + s[last+1:]