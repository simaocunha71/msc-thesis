def check_type(t):
    if len(t) == 0:
        return True
    first_type = type(t[0])
    for item in t:
        if type(item) != first_type:
            return False
    return True