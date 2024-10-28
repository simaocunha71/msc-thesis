    if len(txt)==0:
        return False
    if txt[-1].isalpha():
        if txt[-2]==' ':
            return True
        else:
            return False
    else:
        return False


