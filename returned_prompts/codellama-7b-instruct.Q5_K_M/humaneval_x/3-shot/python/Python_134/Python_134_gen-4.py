    if txt.endswith(" ") or txt.endswith("\n") or txt.endswith("\t"):
        return False
    else:
        if txt[-1].isalpha():
            return True
        else:
            return False