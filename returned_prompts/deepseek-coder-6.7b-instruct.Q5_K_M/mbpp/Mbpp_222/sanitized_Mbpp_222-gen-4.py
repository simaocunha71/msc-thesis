def check_type(t):
    type_check = type(t[0])
    for i in t[1:]:
        if type(i) != type_check:
            return False
    return True