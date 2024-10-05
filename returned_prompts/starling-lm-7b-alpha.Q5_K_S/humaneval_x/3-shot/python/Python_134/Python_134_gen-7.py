    if txt == '':
        return False
    if txt[-1].isalpha() and txt.rfind(' ', 0, len(txt)) == len(txt) - 1:
        return True
    else:
        return False


