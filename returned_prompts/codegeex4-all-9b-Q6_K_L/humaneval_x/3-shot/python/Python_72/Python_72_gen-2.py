    if sum(q) > w:
        return False
    else:
        if q == q[::-1]:
            return True
        else:
            return False

