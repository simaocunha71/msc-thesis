    if not txt:
        return False
    if txt[-1].isalpha():
        if len(txt) == 1 or txt[-2] == ' ':
            return True
    return False


