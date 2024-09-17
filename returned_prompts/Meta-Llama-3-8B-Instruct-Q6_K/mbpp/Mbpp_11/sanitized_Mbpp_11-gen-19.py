def remove_Occ(s, char):
    s = list(s)
    try:
        s.remove(char)
    except ValueError:
        pass
    try:
        s.remove(char)
    except ValueError:
        pass
    return "".join(s)