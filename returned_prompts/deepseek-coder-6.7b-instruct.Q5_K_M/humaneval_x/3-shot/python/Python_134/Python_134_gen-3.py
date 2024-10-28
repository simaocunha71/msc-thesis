    if len(txt) == 0 or txt[-1].isalpha():
        if len(txt.split()) > 1 and txt[-2] == ' ':
            return True
        else:
            return False
    else:
        return False


