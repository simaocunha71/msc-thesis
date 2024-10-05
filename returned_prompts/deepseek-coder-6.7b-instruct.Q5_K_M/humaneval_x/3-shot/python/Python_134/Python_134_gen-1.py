    if len(txt) == 0 or txt[-1].isalpha():
        return False
    if len(txt.split()) < 2:
        return False
    return True


