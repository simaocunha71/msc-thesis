    if len(txt) == 0:
        return False
    else:
        if txt[-1].isalpha() and txt.count(txt[-1]) == 1:
            return True
        else:
            return False


