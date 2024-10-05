
    txt = txt.split(" ")
    if txt[-1] in "abcdefghijklmnopqrstuvwxyz" and len(txt[-1]) == 1:
        return True
    else:
        return False