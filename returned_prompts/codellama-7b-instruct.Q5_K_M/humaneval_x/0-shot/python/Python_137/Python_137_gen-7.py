
def compare_one(a, b):
    if a == b:
        return None
    elif type(a) == type(b) and type(a) == int:
        if a > b:
            return a
        else:
            return b
    elif type(a) == type(b) and type(a) == float:
        if a > b:
            return a
        else:
            return b
    elif type(a) == str and type(b) == str:
        if a > b:
            return a
        else:
            return b
    else:
        return None
