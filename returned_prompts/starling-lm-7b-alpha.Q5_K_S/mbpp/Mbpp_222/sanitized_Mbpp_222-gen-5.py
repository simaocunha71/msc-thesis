def check_type(t):
    for el in t:
        if not isinstance(el, type(t[0])):
            return False
    return True