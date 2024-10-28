    if len(lst) < 2:
        return True
    else:
        if lst[1:] == lst[:-1]:
            return True
        else:
            return False


