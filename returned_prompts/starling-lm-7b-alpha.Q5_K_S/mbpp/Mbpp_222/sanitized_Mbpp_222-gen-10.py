def check_type(t):
    same_type = True
    for elem in t:
        if not isinstance(elem, type(t[0])):
            same_type = False
            break
    return same_type