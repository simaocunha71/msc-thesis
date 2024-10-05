    if txt == "":
        return False
    else:
        return txt[-1].isalpha() and not txt[-1].isupper()


