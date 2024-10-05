    if len(txt) == 0 or not txt[-1].isalpha():
        return False
    if len(txt) == 1 or txt[-2] == ' ':
        return True
    return False

