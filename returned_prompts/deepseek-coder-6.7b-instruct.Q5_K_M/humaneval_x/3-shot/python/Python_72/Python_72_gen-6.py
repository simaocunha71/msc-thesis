    if q != q[::-1]:
        return False
    elif sum(q) <= w:
        return True
    else:
        return False


