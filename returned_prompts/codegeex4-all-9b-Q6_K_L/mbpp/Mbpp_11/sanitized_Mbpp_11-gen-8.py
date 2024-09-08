def remove_Occ(s, c):
    s = s[1:-1]
    first_index = s.find(c)
    last_index = s.rfind(c)
    if first_index != -1:
        s = s[:first_index] + s[first_index+1:]
    if last_index != -1:
        s = s[:last_index] + s[last_index+1:]
    return s