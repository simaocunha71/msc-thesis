    if txt[-1].isalpha() and not txt[-2:].isalnum():
        return True
    else:
        return False


