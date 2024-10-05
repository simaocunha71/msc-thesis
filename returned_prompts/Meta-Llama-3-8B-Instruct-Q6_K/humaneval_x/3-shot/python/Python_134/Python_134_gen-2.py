    if not txt:
        return False
    if txt[-1].isalpha():
        if txt.rstrip().endswith(' '):
            return False
        return True
    return False


