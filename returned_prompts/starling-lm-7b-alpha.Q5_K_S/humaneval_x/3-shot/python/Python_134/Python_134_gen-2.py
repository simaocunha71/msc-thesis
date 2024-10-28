    if len(txt) == 0:
        return False

    if txt[-1].isalpha():
        return True
    else:
        if txt[-1] == ' ':
            return False
        else:
            return False


