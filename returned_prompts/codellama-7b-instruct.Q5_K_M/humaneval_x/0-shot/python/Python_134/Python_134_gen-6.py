    txt = txt.strip()
    return True if txt[-1].isalpha() and txt[-2] in " " else False