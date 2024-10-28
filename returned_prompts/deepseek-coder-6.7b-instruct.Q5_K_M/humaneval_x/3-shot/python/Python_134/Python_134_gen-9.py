    if len(txt) == 0 or txt[-1] == ' ':
        return False
    return txt[-1].isalpha() and txt[-2] == ' '

