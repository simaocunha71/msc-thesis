    if len(txt) == 0 or txt[-1].isalpha() == False:
        return False
    elif len(txt) == 1:
        return True
    elif txt[-2] == " ":
        return True
    return False


