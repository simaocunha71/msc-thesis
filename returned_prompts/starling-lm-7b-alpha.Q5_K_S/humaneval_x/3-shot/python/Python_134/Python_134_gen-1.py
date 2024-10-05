    if len(txt) == 0:
        return False
    if txt[-1].isalpha():
        return True
    else:
        while txt[-1] != ' ':
            txt = txt[:-1]
            if len(txt) == 0:
                return False
        if txt[-1].isalpha():
            return True
        else:
            return False


